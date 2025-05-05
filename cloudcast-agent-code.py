from smolagents import CodeAgent, LiteLLMModel, HfApiModel, ToolCallingAgent, OpenAIServerModel
from tools.visit_web_page_sync_tool import VisitWebPageSyncTool
from tools.atom_feed_find_tool import AtomFeedFindTool
from tools.atom_feed_read_tool import AtomFeedReadTool
from smolagents import FinalAnswerTool
import os
import dotenv

dotenv.load_dotenv()

# model = LiteLLMModel(
#         model_id="ollama/qwen2.5-coder",  # Or try other Ollama-supported models
#         api_base="http://10.0.0.147:11434",  # Default Ollama local server
#         num_ctx=8192,
# )

# HuggingFace
# model = HfApiModel(
#         temperature=0,
#         model_id='Qwen/Qwen2.5-Coder-32B-Instruct'
# )

model = OpenAIServerModel(
    model_id="gpt-4o",
    api_base="https://api.openai.com/v1",
    api_key=os.environ["OPENAI_API_KEY"],
)

# with open("prompt-cloudcast.yaml", "r") as f:
#     prompt_templates = yaml.safe_load(f)

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the Chroma vector store from disk
# vector_store = Chroma(
#     collection_name="langchain",  # Replace with your collection name
#     embedding_function=embeddings,
#     persist_directory="./chroma_db"
# )

agent = CodeAgent(
    model=model,
    tools=[
        VisitWebPageSyncTool(),
    ],
    # prompt_templates=prompt_templates,
    add_base_tools=False,
)

agent_run = agent.run("visit https://www.thecloudcast.net and find all HTML hyper links in podcast archive section", stream=False)
