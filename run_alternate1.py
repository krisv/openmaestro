import asyncio
import time

from app.agent.maestro import Maestro
from app.agent.planning import PlanningAgent
from app.flow.alternate import AlternateFlow
from app.tool.planning import PlanningTool
from app.tool import PlanningTool, Terminate, ToolCollection
from app.logger import logger
from app.schema import Memory, Message
from app.llm_mock import mockLLM

async def run_flow():
    memory: Memory = Memory()
    planningTool = PlanningTool()
    planning_agent = PlanningAgent(memory = memory, available_tools = ToolCollection(planningTool, Terminate()))
    maestro_agent = Maestro(memory = memory)
    agents = {
    }
    try:
        #prompt = input("Enter your prompt: ")

        #if prompt.strip().isspace() or not prompt:
            #logger.warning("Empty prompt provided.")
        
        prompt = "Can you save the organizational structure of everyone reporting to MarkL in a text file?"
        mockLLM._set_scenario("scenario1")

        active_plan_id = f"plan_10005632"
        memory.add_message(Message.user_message(
            f"Create a reasonable plan, with id {active_plan_id}, with clear steps to accomplish the task: {prompt}"))

        flow = AlternateFlow(planning_agent=planning_agent, default_agent=maestro_agent, agents=agents, planning_tool=planningTool, active_plan_id=active_plan_id)
        logger.warning("Processing your request...")

        try:
            start_time = time.time()
            result = await asyncio.wait_for(
                flow.execute(prompt),
                timeout=3600,  # 60 minute timeout for the entire execution
            )
            elapsed_time = time.time() - start_time
            logger.info(f"Request processed in {elapsed_time:.2f} seconds")
            logger.info(result)
        except asyncio.TimeoutError:
            logger.error("Request processing timed out after 1 hour")
            logger.info(
                "Operation terminated due to timeout. Please try a simpler request."
            )

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user.")
    #except Exception as e:
    #   logger.error(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(run_flow())