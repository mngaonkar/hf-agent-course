from typing import Any, Optional
from smolagents.tools import Tool
import re
import json

class ExtractTranscriptContentTool(Tool):
    name = "extract_transcript_content"
    description = "Extract transcript context text from HTML content."
    inputs = {'html_content': {'type': 'string', 'description': 'HTML content to extract the transcript text from'}}
    output_type = "string"

    def forward(self, html_content: str) -> str:
        """Extract transcript context text from HTML content."""
        text_content = []
        matches = re.findall(r'DOCS_modelChunk\s=\s\[(.*?),\s*{', html_content, re.DOTALL)
        if matches is None:
            print("No match found in the HTML content.")
            return ""
        else:
            print("Match found in the HTML content.")
            for match in matches:
                data = json.loads(match)
                if "s" in data:
                    text_content.append(data["s"])

        return ' '.join(text_content)
    
    def __init__(self, *args, **kwargs):
        self.is_initialized = False