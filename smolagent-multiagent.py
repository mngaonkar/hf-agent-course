from smolagents import CodeAgent, LiteLLMModel, HfApiModel, ToolCallingAgent, OpenAIServerModel, DuckDuckGoSearchTool
from tools.visit_web_page_sync_tool import VisitWebPageSyncTool
from tools.atom_feed_find_tool import AtomFeedFindTool
from tools.atom_feed_read_tool import AtomFeedReadTool
from smolagents import FinalAnswerTool
import os
import dotenv

dotenv.load_dotenv()

# model = OpenAIServerModel(
#     model_id="gpt-4o",
#     api_base="https://api.openai.com/v1",
#     api_key=os.environ["OPENAI_API_KEY"],
# )

# HuggingFace
model = HfApiModel(
        temperature=0,
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct'
)

web_agent = ToolCallingAgent(
    model=model,
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebPageSyncTool(),
    ],
    max_steps=10,
    name="web_search_agent",
    description="A web search agent that can search the web and visit web pages.",
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent],
    additional_authorized_imports=["time", "numpy", "pandas", "json"],
)

answer = manager_agent.run("If LLM training continues to scale up at the current rhythm until 2030, what would be the electric power in GW required to power the biggest training runs by 2030? What would that correspond to, compared to some countries? Please provide a source for any numbers used.")