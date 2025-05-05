import os
from smolagents import ToolCollection, CodeAgent, HfApiModel, LiteLLMModel
from mcp import StdioServerParameters

# # HuggingFace
# model = HfApiModel(
#         temperature=0,
#         model_id='Qwen/Qwen2.5-Coder-32B-Instruct'
# )

# Local Ollama
model = LiteLLMModel(
        model_id="ollama/gemma3:12b",  # Or try other Ollama-supported models
        api_base="http://10.0.0.147:11434",  # Default Ollama local server
)

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], model=model, add_base_tools=True)

agent_run = agent.run("summerize the content of http://www.donniedarko.org.uk/philosphy-of-time-travel/", stream=False)