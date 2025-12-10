class MockLLMProvider:
    def __init__(self, name: str):
        self.name = name
    
    def invoke(self, prompt: str) -> str:
        return f"[{self.name} Response] This is a simulated response. In production, this would call the {self.name} API with your query: '{prompt[:50]}...'"
