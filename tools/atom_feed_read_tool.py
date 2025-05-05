from typing import Any, Optional
from smolagents.tools import Tool
import feedparser

class AtomFeedReadTool(Tool):
    name = "atom_feed_read"
    description = "Parse an Atom feed and return the parsed data."
    inputs = {'link': {'type': 'string', 'description': 'A URL to an Atom feed'}}
    output_type = "any"

    def forward(self, link: str) -> Any:
        feed = feedparser.parse(link)
        if feed.bozo:
            raise ValueError(f"Failed to parse feed: {feed.bozo_exception}")
        
        return feed.entries

    def __init__(self, *args, **kwargs):
        self.is_initialized = False