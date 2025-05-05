from playwright.async_api import async_playwright
from typing import Any
from smolagents.tools import Tool
import asyncio
import re

class VisitWebPageTool(Tool):
    name = "visit_webpage"
    description = "Visit a web page and get the text content."
    inputs = {'url': {'type': 'string', 'description': 'Web page URL to visit'},
              'clean_flag': {'type': 'boolean', 'nullable': True, 'description': 'Clean web page text content, this helps to get text from dynamic web page.'}}
    output_type = "string"

    async def __forward(self, url: str, clean_flag=True) -> str:
        async with async_playwright() as p:
            try:
                browser = await p.chromium.launch(headless=False)
                print("browser = ", browser)
                page = await browser.new_page()
                print("page = ", page)
                await page.goto(url, timeout=30000)  # Set a timeout for navigation
                title = await page.title()
                print("page title:", title)
                
                # Extract the text content of the page
                content = await page.content()

                # Extract all text from the page using JavaScript
                all_text = await page.evaluate("""
                    () => {
                        // Get all text nodes from the body
                        const walker = document.createTreeWalker(
                            document.body,
                            NodeFilter.SHOW_TEXT,
                            null,
                            false
                        );
                        let text = '';
                        let node;
                        while (node = walker.nextNode()) {
                            text += node.nodeValue.trim() + ' ';
                        }
                        return text;
                    }
                """)

                # Clean up the text (remove extra spaces, newlines, etc.)
                cleaned_text = re.sub(r'\s+', ' ', all_text).strip()

                await browser.close()
                if clean_flag:
                    return cleaned_text
                else:
                    return content
            except Exception as e:
                await browser.close()
                raise Exception(f"Error visiting webpage: {str(e)}")

    def forward(self, url: str, clean_flag=True) -> str:
        """Visit a web page and get the text content.

        Args:
            url: The URL of the web page to visit.

        Returns:
            str: The text content of the web page.
        """
        try:
            # Run the async __forward method in the event loop
            result = self.__forward(url, clean_flag)
            return result
        except Exception as e:
            return f"Failed to visit webpage: {e}"