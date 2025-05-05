from typing import Any, Optional
from smolagents.tools import Tool
from bs4 import BeautifulSoup

class AtomFeedFindTool(Tool):
    name = "atom_feed_find"
    description = "Parse HTML content find Atom feed links."
    inputs = {'html_content': {'type': 'string', 'description': 'HTML content to extract Atom feed links from'}}
    output_type = "any"

    def forward(self, html_content: str) -> Any:
        feed_links = []
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all <a> tags with "feed" in href
        for link in soup.find_all('a', href=lambda x: x and 'feed' in x.lower()):
            feed_links.append(link.get('href'))
        
        return feed_links

    def __init__(self, *args, **kwargs):
        self.is_initialized = False