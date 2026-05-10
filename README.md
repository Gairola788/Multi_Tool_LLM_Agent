# 🤖 Agentic Multi-Tool AI Assistant

An AI-powered multi-tool assistant built using **LangChain, FastAPI, Streamlit, and Groq LLM**.

This project demonstrates how Large Language Models (LLMs) can intelligently interact with external tools like:

- 🧮 Calculator
- 🌤 Weather API
- 🔎 Internet Search

The system uses:
- ⚡ Smart routing for faster responses
- 🧠 Session-based memory
- 🎨 Interactive Streamlit UI
- 🔄 Fallback handling for tool/API failures

---

## ✨ Why This Project?

This project was built to understand how modern AI agents:
- decide when to use tools,
- manage conversational memory,
- orchestrate APIs,
- and dynamically generate responses.

It focuses on practical AI engineering concepts rather than only building a chatbot UI.

---

# 🚀 Features

## ✅ AI Tool Calling

The LLM dynamically decides which tool to use based on the user's query.

### Examples

| User Query | Tool Used |
|---|---|
| `What is 25 * 10?` | Calculator Tool |
| `What is the weather in Delhi?` | Weather Tool |
| `Explain Python programming` | Search Tool |

---

## ⚡ Smart Routing Optimization

To reduce latency and improve speed:

- Calculator responses skip unnecessary LLM calls
- Weather responses use formatted templates
- Search responses optionally use LLM summarization

This creates a balance between:
- ⚡ Speed
- 🧠 Intelligence
- 💰 Cost efficiency

---

## 🧠 Session-Based Memory

The application stores conversation history using unique `session_id`s.

This enables:
- Multi-user support
- Context-aware conversations
- Persistent interaction flow

---

## 🌐 FastAPI Backend

The backend exposes REST APIs for:
- Chat interactions
- Memory reset
- Agent orchestration

---

## 🎨 Streamlit Frontend

A clean and interactive chat interface built using Streamlit.

Features:
- Chat-style UI
- Real-time interaction
- Reset conversation button
- Loading spinner
- Sidebar-based UI enhancements

---

# 🛠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Core Language |
| LangChain | Agent + Tool Calling |
| Groq API | LLM Inference |
| Llama 3.1 | Language Model |
| FastAPI | Backend Framework |
| Streamlit | Frontend UI |
| OpenWeather API | Weather Data |
| DuckDuckGo API | Internet Search |

---

# 🧠 System Architecture

```text
User
   ↓
Streamlit UI
   ↓
FastAPI Backend
   ↓
LangChain Agent
   ↓
Tool Selection Logic
   ├── 🧮 Calculator Tool
   ├── 🌤 Weather Tool
   └── 🔎 Search Tool
   ↓
Formatted Response
```

---

# 📂 Project Structure

```bash
LLM_Multi_Tool_Agent/
│
├── agent/
│   └── agent.py
│
├── Tools/
│   ├── calculate_tool.py
│   ├── search_tool.py
│   └── weather_tool.py
│
├── assets/
│   ├── homepage.png
│   ├── weather.png
│   ├── calculate.png
│   └── memory.png
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Gairola788/Multi_Tool_LLM_Agent

cd Multi_Tool_LLM_Agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

# 🚀 Running the Application

## Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 📌 API Endpoints

## POST `/chat`

Send user query to the AI agent.

### Request

```json
{
  "question": "What is the weather in Delhi?",
  "session_id": "user123"
}
```

### Response

```json
{
  "response": "🌤 Weather in Delhi..."
}
```

---

## POST `/reset`

Clears memory for a specific session.

Example:

```bash
/reset?session_id=user123
```

---

# 🔥 Engineering Concepts Implemented

- Tool Calling with LangChain
- AI Agent Architecture
- Session-Based Memory
- Smart Routing Optimization
- API Integration
- LLM Optimization
- Error Handling & Fallbacks
- FastAPI Backend Development
- Conversational AI Systems

---

# 📸 Demo Screenshots

## 🖥 Chat UI

![Homepage](assets/homepage.png)

---

## 🌤 Weather Query

![Weather](assets/weather.png)

---

## 🧮 Calculator Query

![Calculator](assets/calculate.png)

---

## 🧠 Memory Feature

![Memory](assets/memory.png)

---

# 🚀 Future Improvements

- ✅ Add RAG Pipeline
- ✅ Add Vector Database (FAISS/Pinecone)
- ✅ Add Authentication
- ✅ Docker Deployment
- ✅ Streaming Responses
- ✅ Voice Assistant Integration
- ✅ Resume Chat Feature
- ✅ Cloud Deployment

---

# 👨‍💻 Author

### Akshat  
B.Tech CSE (AI/ML)

Passionate about:
- AI Engineering
- NLP
- Agentic AI
- Backend Development

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!