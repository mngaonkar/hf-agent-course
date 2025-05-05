from playwright.sync_api import sync_playwright
from smolagents.tools import Tool
import re

class VisitWebPageSyncTool(Tool):
    name = "visit_webpage"
    description = "Visit a web page and get the text content."
    inputs = {'url': {'type': 'string', 'description': 'Web page URL to visit'},
              'deep_flag': {'type': 'boolean', 'nullable': True, 'description': 'Dig deep for text content, this helps to get text from dynamic web page.'}}
    output_type = "string"

    def forward(self, url: str, deep_flag=True) -> str:
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=False)
                print("browser = ", browser)
                page = browser.new_page()
                print("page = ", page)
                page.goto(url, timeout=30000)  # Set a timeout for navigation
                title = page.title()
                print("page title:", title)
                
                # Extract the text content of the page
                # content = page.text_content("body")
                content = page.locator("body").inner_text()

                # Extract all text from the page using JavaScript
                all_text = page.evaluate("""
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

                browser.close()
                if deep_flag:
                    return cleaned_text
                else:
                    return content
            except Exception as e:
                browser.close()
                raise Exception(f"Error visiting webpage: {str(e)}")