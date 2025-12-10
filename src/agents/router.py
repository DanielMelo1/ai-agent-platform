from src.providers.mock_provider import MockLLMProvider

class LLMRouter:
    def __init__(self):
        self.claude = MockLLMProvider("Claude")
        self.gemini = MockLLMProvider("Gemini")
    
    def classify_complexity(self, query: str) -> str:
        word_count = len(query.split())
        return "simple" if word_count < 15 else "complex"
    
    def route(self, query: str) -> dict:
        complexity = self.classify_complexity(query)
        provider = "gemini" if complexity == "simple" else "claude"
        llm = self.gemini if complexity == "simple" else self.claude
        
        return {
            "provider": provider,
            "complexity": complexity,
            "response": llm.invoke(query),
            "note": "Demo mode - Replace MockLLMProvider with real API keys"
        }
