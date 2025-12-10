from langchain_google_genai import ChatGoogleGenerativeAI
import os

class GeminiProvider:
    def __init__(self, model: str = "gemini-1.5-flash"):
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
    
    def invoke(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content
