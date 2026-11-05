import yaml
import sys
import os

# This helps Python find the 'agents' and 'evals' folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.simple_agent import get_agent_response
from evals.scorer import score_response

def run_evaluation():
    print("Starting Evaluation...\n")
    
    # Read the YAML file
    with open('tasks/example.yaml', 'r') as file:
        data = yaml.safe_load(file)
        
    tasks = data['tasks']
    passed_count = 0
    total_count = len(tasks)
    
    # Loop through each task
    for task in tasks:
        prompt = task['input']
        expected = task['expected']
        
        # Get the agent's answer
        answer = get_agent_response(prompt)
        
        # Score the answer
        is_correct = score_response(answer, expected)
        
        if is_correct:
            passed_count += 1
            status = "✅ PASS"
        else:
            status = "❌ FAIL"
            
        print(f"--- {task['id']} [{status}] ---")
        print(f"Prompt:   {prompt}")
        print(f"Expected: {expected}")
        print(f"Agent:    {answer}\n")
        
    # Print final summary
    print("===================================")
    print(f"FINAL RESULTS: {passed_count}/{total_count} passed")
    pass_rate = (passed_count / total_count) * 100
    print(f"Pass Rate: {pass_rate:.1f}%")
    print("===================================")

if __name__ == "__main__":
    run_evaluation()