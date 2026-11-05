import yaml
import sys
import os
import json
import datetime

# This helps Python find the 'agents' and 'evals' folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.simple_agent import get_agent_response
from evals.scorer import score_response

def run_evaluation():
    print("Starting Evaluation...\n")
    
    with open('tasks/example.yaml', 'r') as file:
        data = yaml.safe_load(file)
        
    tasks = data['tasks']
    passed_count = 0
    total_count = len(tasks)
    results_data = []
    
    for task in tasks:
        prompt = task['input']
        expected = task['expected']
        answer = get_agent_response(prompt)
        is_correct = score_response(answer, expected)
        
        if is_correct:
            passed_count += 1
            status = "✅ PASS"
        else:
            status = "❌ FAIL"
            
        print(f"--- {task['id']} [{status}] ---")
        
        # Save individual task result to a list
        results_data.append({
            "id": task['id'],
            "prompt": prompt,
            "expected": expected,
            "agent_answer": answer,
            "passed": is_correct
        })
        
    pass_rate = (passed_count / total_count) * 100
    
    # Create the final report dictionary
    report = {
        "timestamp": str(datetime.datetime.now()),
        "total_tasks": total_count,
        "passed": passed_count,
        "pass_rate": round(pass_rate, 1),
        "results": results_data
    }
    
    # Save to JSON file
    os.makedirs('reports', exist_ok=True)
    with open('reports/latest_eval.json', 'w') as f:
        json.dump(report, f, indent=4)
        
    print("===================================")
    print(f"FINAL RESULTS: {passed_count}/{total_count} passed")
    print(f"Pass Rate: {pass_rate:.1f}%")
    print("Report saved to reports/latest_eval.json")
    print("===================================")

if __name__ == "__main__":
    run_evaluation()