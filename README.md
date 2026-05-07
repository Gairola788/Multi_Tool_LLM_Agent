🤖 Multi-Tool AI Agent
An AI-powered multi-tool assistant built using LangChain, FastAPI, Streamlit, and Ollama.
This project demonstrates how Large Language Models (LLMs) can intelligently interact with external tools like:


🧮 Calculator


🌤 Weather API


🔎 Internet Search


The system uses:


⚡ Smart routing for faster responses


🧠 Session-based memory


🎨 Interactive Streamlit UI


🔄 Fallback handling for tool/API failures



🚀 Features
✅ AI Tool Calling
The LLM dynamically decides which tool to use based on the user's query.
Examples
User QueryTool UsedWhat is 25 * 10?Calculator ToolWhat is the weather in Delhi?Weather ToolExplain Python programmingSearch Tool

⚡ Smart Routing Optimization
To reduce latency and improve speed:


Calculator responses skip unnecessary LLM calls


Weather responses use formatted templates


Search responses optionally use LLM summarization


This creates a balance between:


⚡ Speed


🧠 Intelligence


💰 Cost efficiency



🧠 Session-Based Memory
The application stores conversation history using unique session_ids.
This enables:


Multi-user support


Context-aware conversations


Persistent interaction flow



🌐 FastAPI Backend
The backend exposes REST APIs for:


Chat interactions


Memory reset


Agent orchestration



🎨 Streamlit Frontend
A clean and interactive chat interface built using Streamlit.
Features:


Chat-style UI


Real-time interaction


Reset conversation button


Loading spinner



🛠 Tech Stack
TechnologyUsagePythonCore LanguageLangChainAgent + Tool CallingOllamaLocal LLM RuntimeMistral / Llama3Language ModelsFastAPIBackend FrameworkStreamlitFrontend UIOpenWeather APIWeather DataDuckDuckGo APIInternet Search

🧠 System Architecture
User  ↓Streamlit UI  ↓FastAPI Backend  ↓LangChain Agent  ↓Tool Selection  ├── 🧮 Calculator Tool  ├── 🌤 Weather Tool  └── 🔎 Search Tool  ↓Formatted Response

📂 Project Structure
LLM-Multi-Tool-Agent/│├── agent/│   └── agent.py│├── Tools/│   ├── calculate_tool.py│   ├── search_tool.py│   └── weather_tool.py│├── main.py├── streamlit_app.py├── requirements.txt├── README.md├── .gitignore└── .env

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/LLM-Multi-Tool-Agent.gitcd LLM-Multi-Tool-Agent

2️⃣ Create Virtual Environment
Windows
python -m venv venvvenv\Scripts\activate
Linux / Mac
python3 -m venv venvsource venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables
Create a .env file:
OPENWEATHER_API_KEY=your_api_key_here

🤖 Setup Ollama
Install Ollama:
Ollama Official Website
Pull model:
ollama pull mistral
Run Ollama server:
ollama serve

🚀 Running the Application
Start FastAPI Backend
uvicorn main:app --reload
Backend URL:
http://127.0.0.1:8000

Start Streamlit Frontend
streamlit run streamlit_app.py
Frontend URL:
http://localhost:8501

📌 API Endpoints
POST /chat
Send user query to the AI agent.
Request
{  "question": "What is the weather in Delhi?",  "session_id": "user123"}
Response
{  "response": "🌤 Weather in Delhi..."}

POST /reset
Clears memory for a specific session.
Example:
/reset?session_id=user123

🔥 Engineering Concepts Implemented


Tool Calling with LangChain


AI Agent Architecture


Session-Based Memory


Smart Routing Optimization


API Integration


LLM Optimization


Error Handling & Fallbacks


FastAPI Backend Development



📸 Demo Screenshots
Chat UI
Add screenshot here:screenshots/chat_ui.png
Weather Query
Add screenshot here:screenshots/weather_demo.png
Calculator Query
Add screenshot here:screenshots/calculator_demo.png

🚀 Future Improvements


✅ Add RAG Pipeline


✅ Add Vector Database (FAISS/Pinecone)


✅ Add Authentication


✅ Docker Deployment


✅ Streaming Responses


✅ Voice Assistant Integration


✅ Cloud Deployment



👨‍💻 Author
Akshat
B.Tech CSE (AI/ML)
Passionate about:


AI Engineering


NLP


Agentic AI


Backend Development



⭐ Support
If you found this project useful, consider giving it a ⭐ on GitHub!