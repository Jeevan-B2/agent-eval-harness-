import streamlit as st
import json
import os
import subprocess

st.set_page_config(page_title="Agent Eval Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 Agent Evaluation Dashboard")
st.markdown("This dashboard visualizes the performance of the LLM Agent against the test suite.")

# Path to the report
report_path = 'reports/latest_eval.json'

# Add a button to run the evaluation right from the dashboard
if st.button("🚀 Run New Evaluation"):
    with st.spinner("Running evaluation..."):
        subprocess.run(["python", "evals/runner.py"])
    st.success("Evaluation complete!")

if os.path.exists(report_path):
    with open(report_path, 'r') as f:
        report = json.load(f)
        
    st.divider()
    
    # Display Top Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tasks", report['total_tasks'])
    col2.metric("Tasks Passed", report['passed'])
    col3.metric("Pass Rate", f"{report['pass_rate']}%")
    
    st.divider()
    
    # Display the results table
    st.subheader("Detailed Results")
    
    # Prepare data for the table
    table_data = []
    for res in report['results']:
        status_icon = "✅" if res['passed'] else "❌"
        table_data.append({
            "ID": res['id'],
            "Status": status_icon,
            "Prompt": res['prompt'],
            "Expected": res['expected'],
            "Agent Answer": res['agent_answer']
        })
        
    st.dataframe(table_data, use_container_width=True)
    st.caption(f"Last run: {report['timestamp']}")

else:
    st.warning("No evaluation report found. Click 'Run New Evaluation' to generate one.")