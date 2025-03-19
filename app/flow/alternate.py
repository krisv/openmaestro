import json
import time
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

from app.agent.base import BaseAgent
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
    agents: List[BaseAgent] = None
    planning_tool: PlanningTool = None

    async def execute(self, input_text: str) -> str:
        """Execute the planning flow with agents."""
        try:
            result = ""
            stepCount = 0
            while True:
                # Get current step to execute
                #self.current_step_index, step_info = await self._get_current_step_info()
                logger.info(f"Executing AlternateFlow {stepCount}")
                stepCount += 1
                if (stepCount == self.max_steps):
                    break

                for agent in self.agents:
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
        except Exception as e:
            logger.error(f"Error in PlanningFlow: {str(e)}")
            return f"Execution failed: {str(e)}"

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
