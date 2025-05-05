from huggingface_hub import list_models
from smolagents import Tool

class ModelDownloadTool(Tool):
    name = "most_downloaded_model"
    description = """Returns the most downloaded model for a specific task on the Hugging Face Hub."""
    inputs = {'task': {'type': 'string', 'description': 'The task (e.g., text-classification, text-to-video).'}}
    output_type = "string"

    def forward(self, task: str) -> str:
        """Returns the most downloaded model for a specific task on the Hugging Face Hub.
        
        Args:
            task: The task (e.g., 'text-classification', 'text-to-video').
        
        Returns:
            str: The ID of the most downloaded model for the specified task.
        """
        model = next(iter(list_models(task=task, sort="downloads")), None)
        return model.id
    
