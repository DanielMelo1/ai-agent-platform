from langchain_anthropic import ChatAnthropic
from typing import Optional
import os

class ClaudeProvider:
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.llm = ChatAnthropic(
            model=model,
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            max_tokens=1024
        )
    
    def invoke(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content
