def get_agent_response(prompt: str) -> str:
    """
    A simple rule-based agent for testing.
    Later, this can be replaced with a real LLM.
    """
    prompt_lower = prompt.lower()
    
    if "capital of france" in prompt_lower:
        return "The capital of France is Paris."
    elif "15 multiplied by 4" in prompt_lower:
        return "The answer is 60."
    elif "add two numbers" in prompt_lower:
        return "def add(a, b): return a + b"
    elif "opposite of 'hot'" in prompt_lower:
        return "The opposite is cold."
    elif "translate 'hello'" in prompt_lower:
        return "Hola"
    else:
        return "I don't know."