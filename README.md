# 🔍 Analyzer Agent using AutoGen

This project implements a **multi-agent system** for **data analysis and code execution** using [Microsoft AutoGen](https://microsoft.github.io/autogen/).  
It brings together specialized agents that collaborate in a **Round-Robin group chat** to analyze structured data and execute Python code in a controlled Docker environment.

---

## 🚀 Features
- 🤖 **Data Analyzer Agent**: Interprets CSV/structured data, performs analysis, and suggests next steps.  
- ⚙️ **Code Executor Agent**: Executes Python code safely in Docker, returning results back to the team.  
- 🔄 **Round-Robin Group Chat**: Agents take turns in a collaborative loop until conditions are met.  
- 🛑 **Custom Termination**: Stops execution when the `STOP` keyword is mentioned or after a max number of turns.  
- 🧩 **Extensible**: Easily add more agents (e.g., visualization, SQL analysis) to the workflow.  

---

## 🏗️ Architecture
- **`Data_analyzer_agent`**: Uses LLM reasoning to analyze data and propose actions.  
- **`Code_executor_agent`**: Runs generated Python snippets inside Docker for reproducibility and safety.  
- **Team Orchestration**: Managed via `RoundRobinGroupChat` from AutoGen.  

Workflow:
1. Data Analyzer Agent inspects input data.  
2. Suggests transformations, computations, or visualizations.  
3. Code Executor Agent executes and returns results.  
4. Loop continues until termination (`STOP` keyword or max turns).  

---

## 📂 Project Structure
