from typing import Any, Optional
from smolagents.tools import Tool
from bs4 import BeautifulSoup

class ExtractTranscriptLinkTool(Tool):
    name = "extract_transcript_link"
    description = "Extract transcript link from HTML content."
    inputs = {'content': {'type': 'string', 'description': 'HTML content to extract the transcript link from'}}
    output_type = "any"

    def forward(self, content: str) -> Any:
        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')

        # Find the anchor tag after the <b>SHOW TRANSCRIPT: </b>
        transcript_tag = soup.find('b', string="SHOW TRANSCRIPT: ")
        if transcript_tag is None:
            print("Transcript tag not found.")
            return None
        link_tag = transcript_tag.find_next('a')

        # Extract the href attribute
        transcript_url = link_tag['href'] if link_tag else None

        print("Transcript URL:", transcript_url)
        return transcript_url

    def __init__(self, *args, **kwargs):
        self.is_initialized = False