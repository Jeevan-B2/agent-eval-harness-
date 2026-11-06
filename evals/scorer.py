import string

def score_response(agent_answer: str, expected_answer: str) -> bool:
    if not agent_answer or not expected_answer:
        return False
        
    # 1. Convert to lowercase
    agent_clean = str(agent_answer).lower()
    expected_clean = str(expected_answer).lower()
    
    # 2. Remove ALL spaces and newlines
    agent_clean = "".join(agent_clean.split())
    expected_clean = "".join(expected_clean.split())
    
    # 3. Remove all punctuation (periods, commas, quotes, etc.)
    for p in string.punctuation:
        agent_clean = agent_clean.replace(p, "")
        expected_clean = expected_clean.replace(p, "")
        
    # 4. Check if the expected answer is inside the AI's answer
    return expected_clean in agent_clean