from smolagents import CodeAgent, Tool, LiteLLMModel, HfApiModel, DuckDuckGoSearchTool, ToolCallingAgent, FinalAnswerTool
import dotenv
from smolagents import OpenAIServerModel
import os
from tools.visit_web_page_sync_tool import VisitWebPageSyncTool
from smolagents import VisitWebpageTool
import litellm

dotenv.load_dotenv()

# OpenAI
# model = OpenAIServerModel(
#     model_id="gpt-4o",
#     api_base="https://api.openai.com/v1",
#     api_key=os.environ["OPENAI_API_KEY"],
# )

# Local Ollama
model = LiteLLMModel(
        model_id="ollama/gemma3:12b",  # Or try other Ollama-supported models
        api_base="http://10.0.0.147:11434",  # Default Ollama local server
)

# litellm._turn_on_debug()

# HuggingFace
# model = HfApiModel(
#         temperature=0,
#         model_id='Qwen/Qwen2.5-Coder-32B-Instruct'
# )

# agent = CodeAgent(
#     tools=[VisitWebPageSyncTool()],
#     # tools=[DuckDuckGoSearchTool()],
#     model=model
# )

agent = ToolCallingAgent(
    # tools=[VisitWebpageTool()],
    tools=[VisitWebPageSyncTool(), FinalAnswerTool()],
    # tools=[DuckDuckGoSearchTool()],
    model=model
)

agent_run = agent.run("summerize the content of http://www.donniedarko.org.uk/philosphy-of-time-travel/ with deep_flag False", stream=False)