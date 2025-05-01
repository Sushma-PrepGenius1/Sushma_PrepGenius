from typing import List
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

def listAvailableModels(apiKey: str) -> List[str]:
    """
    Retrieves a list of available model names from the Gemini API.

    Args:
        apiKey (str): Your Gemini API key.

    Returns:
        List[str]: A list of available model names.

    Raises:
        GoogleAPIError: If an error occurs while fetching the models.
    """
    try:
        genai.configure(api_key=apiKey)
        models = genai.list_models()
        modelNames = [model.name for model in models]
        return modelNames
    except GoogleAPIError as error:
        print(f"An error occurred while listing models: {error}")
        return []






if __name__ == "__main__":
    apiKey = "AIzaSyDXX5WRHlWICkoQ71pcz4wnrd8TKbn-D-Y"  # Replace with your actual API key
    availableModels = listAvailableModels(apiKey)
    if availableModels:
        print("Available Models:")
        for modelName in availableModels:
            print(f"- {modelName}")
    else:
        print("No models available or an error occurred.")
