from typing import Optional

from app.agent.toolcall import ToolCallAgent
from app.prompt.maestro import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.tool import DataLookup, FileSaver, Terminate, ToolCollection

from pydantic import Field

class Maestro(ToolCallAgent):
    """
    A versatile general-purpose agent that uses planning to solve various tasks.

    This agent extends PlanningAgent with a comprehensive set of tools and capabilities,
    including Python execution, web browsing, file operations, and information retrieval
    to handle a wide range of user requests.
    """

    name: str = "Maestro"
    description: str = (
        "A versatile agent that can solve various tasks using multiple tools"
    )

    system_prompt: str = SYSTEM_PROMPT
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 2000
    max_steps: int = 1

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            #PythonExecute(), WebSearch(), BrowserUseTool(),
            FileSaver(), Terminate(), DataLookup()
        )
    )

    #async def _handle_special_tool(self, name: str, result: Any, **kwargs):
    #    if not self._is_special_tool(name):
    #        return
    #    else:
    #        await self.available_tools.get_tool(BrowserUseTool().name).cleanup()
    #        await super()._handle_special_tool(name, result, **kwargs)

    #def _is_special_tool(self, name: str) -> bool:
    #    # Meastro should yield after each tool execution, so planner can update.
    #    return True


    #async def run(self, request: Optional[str] = None) -> str:
    #    print(f"Starting agent run for request {request}")
    #    return "Nothing to do"