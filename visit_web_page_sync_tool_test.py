from tools.visit_web_page_sync_tool import VisitWebPageSyncTool
from markdownify import markdownify as md
page_content = VisitWebPageSyncTool()("https://www.thecloudcast.net", deep_flag=True)
print(md(page_content).strip())