from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import model_name
from dotenv import load_dotenv
import os  
load_dotenv()



def get_model_client():

    model_client = OpenAIChatCompletionClient(
        model=model_name,
        #api_key="GEMINI_API_KEY",
        model_info= {
        "family": "gemini-2.5-pro",
        "vision": False,
        "function_calling": True,
        "json_output": True
    }

    )
    return model_client

