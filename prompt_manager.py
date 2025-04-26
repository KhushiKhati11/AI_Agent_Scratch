from typing import List ,Optional   #specify the type of elements in List and for a variable of type x or None
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class PromptManager:
    
    def __init__(self, input_variables: List[str], template: str):
        # To initializes the PromptManager with the required template.
        # input_variables :List of variables to be formatted and template:Template string with placeholders.
        self.prompt_template = PromptTemplate(
            input_variables=input_variables,
            template=template
        )

    def format_prompt(self, **kwargs) -> str:
        # Formats the prompt with provided keyword arguments.
        try:
            prompt_value = self.prompt_template.format_prompt(**kwargs)
            return prompt_value.to_string()
        except Exception as e:
            raise ValueError(f"Error formatting prompt: {e}")

    def get_template(self) -> str:
        # Returns the base template 
        return self.prompt_template.template
    

# A tool for PromptManager
class PromptTool(BaseTool):
    name: str = "PromptFormatter"
    description: str = "Formats a question into a standardized prompt."
    prompt_manager: PromptManager

    def _run(self, question: str) -> str:
        try:
            return self.prompt_manager.format_prompt(question=question)
        except Exception as e:
            return f"Error in PromptTool: {e}"
        
    async def _arun(self, question: str) -> str:
        # Asynchronous execution (optional, usually not needed unless using async agents).
        raise NotImplementedError("Async version not implemented.")
    
    
