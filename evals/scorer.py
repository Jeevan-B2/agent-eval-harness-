def score_response(agent_answer: str, expected_answer: str) -> bool:
    """
    Grades the agent's answer.
    For now, it checks if the expected answer is inside the agent's answer.
    It ignores uppercase/lowercase differences.
    """
    if not agent_answer:
        return False
        
    agent_clean = str(agent_answer).strip().lower()
    expected_clean = str(expected_answer).strip().lower()
    
    # If the expected answer is found in the agent's answer, it's a pass!
    return expected_clean in agent_clean