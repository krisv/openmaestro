import os

import aiofiles

from app.tool.base import BaseTool


class DataLookup(BaseTool):
    name: str = "data_lookup"
    description: str = """Look up additional data from various sources.
Use this tool when you need to find data around a specific topic.
The tool accepts a data source name, and a query.
"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "source": {
                "type": "string",
                "description": "(required) The name of the source to query.",
            },
            "query": {
                "type": "string",
                "description": "(required) The query to pass to the source to find the relevant information.",
            },
        },
        "required": ["source", "query"],
    }

    async def execute(self, source: str, query: str) -> str:
        """
        Look up data from the given source based on the given query.

        Args:
            source (str): The name of the source.
            query (str): The query to find the data you need.

        Returns:
            str: The data requested.
        """
        result = """
            Kris Verlaenen reports to Mark Proctor
            Mark Proctor reports to Mark Little
            Ricardo Zanini reports to David Gutierrez
            Francisco Javier Tirado Sarti reports to David Gutierrez 
            David Gutierrez reports to Mark Little
            Mario Fusco reports to Marek Novotny
            Marek reports to Mark Little
            """
        return result
