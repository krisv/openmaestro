import json
import time
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

from app.agent.base import BaseAgent
from app.agent.planning import PlanningAgent
from app.flow.base import BaseFlow, PlanStepStatus
from app.llm import LLM
from app.logger import logger
from app.schema import AgentState, Message, ToolChoice
from app.tool import PlanningTool


class AlternateFlow(BaseModel):
    """A flow that manages planning and execution of tasks using agents."""

    active_plan_id: str = Field(default_factory=lambda: f"plan_{int(time.time())}")
    current_step_index: Optional[int] = None
    max_steps: int = 20
    planning_agent: PlanningAgent = None
    default_agent: BaseAgent = None
    agents: Dict[str, BaseAgent] = None
    planning_tool: PlanningTool = None

    async def execute(self, input_text: str) -> str:
        """Execute the planning flow with agents."""
        #try:
        result = ""
        stepCount = 0
        await self.planning_agent.load_plan_definition(input_text)
            
        while True:
            # Get current step to execute
            #self.current_step_index, step_info = await self._get_current_step_info()
            logger.info(f"Executing AlternateFlow {stepCount}")
            stepCount += 1
            if (stepCount == self.max_steps):
                break

            logger.info(f"Executing planning agent")
            step_result = await self._execute_step(self.planning_agent)
            result += step_result + "\n"
            if self.planning_tool._is_plan_completed(self.active_plan_id):
                break
            
            type = "default"
            current_step_index, step_info = await self._get_current_step_info()
            step_type = step_info.get("type") if step_info else None
            agent = self.default_agent
            if step_type:
                if step_type in self.agents:
                    agent = self.agents[step_type]
                    logger.info(f"Found task type {step_type} and agent {agent.name}")
                else:
                    logger.info(f"Could not find agent for task type {step_type}, using default")

            logger.info(f"Executing agent {agent.name}")
            step_result = await self._execute_step(agent)

            if self.planning_tool._is_plan_completed(self.active_plan_id):
                break

            result += step_result + "\n"

            # Check if agent wants to terminate
            if self.planning_tool._is_plan_completed(self.active_plan_id):
                result += self.planning_tool._get_plan(self.active_plan_id).output
                break

        return result
        #except Exception as e:
        #    logger.error(f"Error in PlanningFlow: {e}")
        #    return f"Execution failed: {str(e)}"

    async def _execute_step(self, agent: BaseAgent) -> str:
        """Execute the current step with the specified agent using agent.run()."""
        # Prepare context for the agent with current plan status
        #plan_status = await self._get_plan_text()
        #step_text = step_info.get("text", f"Step {self.current_step_index}")

        # Create a prompt for the agent to execute the current step
        #step_prompt = f"""
        #CURRENT PLAN STATUS:
        #{plan_status}

        #CURRENT TASK:
        #We are on step {self.current_step_index}: "{step_text}"
        #"""

        # Use agent.run() to execute the step
        try:
            step_result = await agent.run()
            return step_result
        except Exception as e:
            logger.error(f"Error executing step: {e}")
            return f"Error executing step: {str(e)}"

    async def _finalize_plan(self) -> str:
        """Finalize the plan and provide a summary using the flow's LLM directly."""
        plan_text = await self._get_plan_text()

        # Create a summary using the flow's LLM directly
        try:
            system_message = Message.system_message(
                "You are a planning assistant. Your task is to summarize the completed plan."
            )

            user_message = Message.user_message(
                f"The plan has been completed. Here is the final plan status:\n\n{plan_text}\n\nPlease provide a summary of what was accomplished and any final thoughts."
            )

            response = await self.llm.ask(
                messages=[user_message], system_msgs=[system_message]
            )

            return f"Plan completed:\n\n{response}"
        except Exception as e:
            logger.error(f"Error finalizing plan with LLM: {e}")

            # Fallback to using an agent for the summary
            try:
                agent = self.primary_agent
                summary_prompt = f"""
                The plan has been completed. Here is the final plan status:

                {plan_text}

                Please provide a summary of what was accomplished and any final thoughts.
                """
                summary = await agent.run(summary_prompt)
                return f"Plan completed:\n\n{summary}"
            except Exception as e2:
                logger.error(f"Error finalizing plan with agent: {e2}")
                return "Plan completed. Error generating summary."

    async def _get_current_step_info(self) -> tuple[Optional[int], Optional[dict]]:
        """
        Parse the current plan to identify the first non-completed step's index and info.
        Returns (None, None) if no active step is found.
        """
        if (
            not self.active_plan_id
            or self.active_plan_id not in self.planning_tool.plans
        ):
            logger.error(f"Plan with ID {self.active_plan_id} not found")
            return None, None

        try:
            # Direct access to plan data from planning tool storage
            plan_data = self.planning_tool.plans[self.active_plan_id]
            steps = plan_data.get("steps", [])
            step_statuses = plan_data.get("step_statuses", [])

            # Find first non-completed step
            for i, step in enumerate(steps):
                if i >= len(step_statuses):
                    status = PlanStepStatus.NOT_STARTED.value
                else:
                    status = step_statuses[i]

                if status in PlanStepStatus.get_active_statuses():
                    # Extract step type/category if available
                    step_info = {"text": step}

                    # Try to extract step type from the text (e.g., [SEARCH] or [CODE])
                    import re

                    type_match = re.search(r"\[([A-Za-z_]+)\]", step)
                    if type_match:
                        step_info["type"] = type_match.group(1).lower()

                    # Mark current step as in_progress
                    try:
                        await self.planning_tool.execute(
                            command="mark_step",
                            plan_id=self.active_plan_id,
                            step_index=i,
                            step_status=PlanStepStatus.IN_PROGRESS.value,
                        )
                    except Exception as e:
                        logger.warning(f"Error marking step as in_progress: {e}")
                        # Update step status directly if needed
                        if i < len(step_statuses):
                            step_statuses[i] = PlanStepStatus.IN_PROGRESS.value
                        else:
                            while len(step_statuses) < i:
                                step_statuses.append(PlanStepStatus.NOT_STARTED.value)
                            step_statuses.append(PlanStepStatus.IN_PROGRESS.value)

                        plan_data["step_statuses"] = step_statuses

                    return i, step_info

            return None, None  # No active step found

        except Exception as e:
            logger.warning(f"Error finding current step index: {e}")
            return None, None