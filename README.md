# LLM Multi Tool Agent

## 📌 Project Overview

This project implements a **Multi-Tool AI Agent powered by an LLM** that can intelligently decide which tool to use based on the user’s query.

Instead of manually selecting tools, the **LLM analyzes the user's request and calls the appropriate tool automatically**.

The agent currently supports three tools:

* Calculator Tool
* Weather Tool
* Web Search Tool

The system is built using **LangChain with a local LLM running through Ollama**.

---

## ⚙️ Features

* LLM based tool selection
* Multi-tool architecture
* Real-time weather data using API
* Web search capability
* Mathematical calculations
* Modular tool design

---

## 🧠 How the Agent Works

User Query
↓
LLM analyzes the request
↓
LLM selects the appropriate tool
↓
Tool executes the task
↓
Result is returned to the LLM
↓
LLM generates the final response

---

## 🛠️ Tech Stack

* Python
* LangChain
* Ollama (Local LLM)
* OpenWeather API
* Requests Library
* python-dotenv

---

## 📂 Project Structure

```
LLM_MultiTool_Agent
│
├── main.py
├── Tools
│   ├── calculate_tool.py
│   ├── weather_tool.py
│   └── search_tool.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

Clone the repository:

```
git clone <your_repo_url>
cd LLM_MultiTool_Agent
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add your API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

Run the agent:

```
python main.py
```

Example interaction:

```
Ask any query: What is the weather in Delhi?
Ask any query: Calculate 45 * 23
Ask any query: What does IPL stand for in cricket?
```

---

## 📖 Example Tool Usage

| User Query              | Tool Used       |
| ----------------------- | --------------- |
| Calculate 10 + 5        | Calculator Tool |
| Weather in London       | Weather Tool    |
| What is IPL in cricket? | Search Tool     |

---

## 🚀 Future Improvements

* Add conversational memory
* Integrate vector database for knowledge retrieval
* Improve tool descriptions
* Add more external tools
* Build a web interface

---

## 👨‍💻 Author

Akshat

