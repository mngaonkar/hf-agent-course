import requests
from typing import Any
from smolagents.tools import Tool
from markdownify import markdownify

class VisitWebPageTool(Tool):
    name = "visit_webpage"
    description = "Visit a web page and get the text content."
    inputs = {'url': {'type': 'string', 'description': 'Web page URL to visit'}}
    output_type = "string"

    def forward(self, url: str) -> str:
        """Visit a web page and get the text content.

        Args:
            url: The URL of the web page to visit.

        Returns:
            str: The text content of the web page.
        """
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Raise an error for bad responses
            markdown_content = markdownify(response.text).strip()
            return markdown_content
        except requests.RequestException as e:
            return f"Failed to visit webpage: {e}"