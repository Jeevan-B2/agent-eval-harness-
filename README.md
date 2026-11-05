# Agent Eval Harness 🤖

An automated evaluation and regression-testing system for LLM Agents. 

## 📌 The Problem
When building AI agents, making a prompt change can unexpectedly break the agent's ability to follow instructions. Without automated testing, developers have no way to know if their agent got better or worse. 

## 💡 The Solution
This project provides an **Evaluation Harness** that runs an AI agent against a fixed suite of tasks, scores the results automatically, and reports the pass rate. It includes a CI/CD pipeline that runs these tests on every GitHub push to catch regressions.

## 🏗️ Architecture
1. **Tasks (`tasks/example.yaml`):** A suite of 10 test cases (prompts and expected answers).
2. **Agent (`agents/simple_agent.py`):** The AI model being tested.
3. **Runner & Scorer (`evals/`):** The engine that runs the tasks, scores the answers, and generates a JSON report.
4. **CI/CD (`.github/workflows/eval.yml`):** GitHub Actions pipeline that runs the evaluation on every push.
5. **Dashboard (`app.py`):** A Streamlit web interface to visualize the results.

## 🚀 Live Demo (Dashboard)
*(Take a screenshot of your Streamlit dashboard and drag-and-drop it here on GitHub to generate a link. It should look like this:)*
![Dashboard Screenshot](YOUR_IMAGE_LINK_HERE)

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit** & **Pandas** (for the dashboard)
- **PyYAML** (for test configuration)
- **GitHub Actions** (for CI/CD)

## 💻 How to Run Locally
1. Clone the repo: `git clone https://github.com/Jeevan-B2/agent-eval-harness-.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the evaluation script: `python evals/runner.py`
4. Launch the dashboard: `streamlit run app.py`

## 📊 CI/CD Pipeline
This repository uses GitHub Actions. On every push to the `main` branch, the agent is evaluated against the test suite. If the agent fails the tasks, the CI pipeline will fail, preventing bad code from being merged.