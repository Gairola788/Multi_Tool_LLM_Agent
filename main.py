from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent.agent import run_agent, create_memory, trim_memory

app = FastAPI()

memory_store = {}

# ------------------ REQUEST SCHEMA ------------------

class Query(BaseModel):
    question: str
    session_id: str = "default"

# ------------------ API ENDPOINT ------------------

@app.post("/chat")
def chat(query: Query):

    try:
        session_id = query.session_id

        # Create memory if new session
        if session_id not in memory_store:
            memory_store[session_id] = create_memory()

        messages = memory_store[session_id]

        # Run agent
        response, messages = run_agent(query.question, messages)

        # Trim memory
        messages = trim_memory(messages)

        # Save memory
        memory_store[session_id] = messages

        print("FINAL RESPONSE:", response)

        return {"response": response}

    except Exception as e:
        import traceback

        print("========== ERROR ==========")
        traceback.print_exc()
        print("===========================")

        return {"response": f"Backend Error: {str(e)}"}


# ------------------ RESET MEMORY ------------------

@app.post("/reset")
def reset(session_id: str = "default"):
    if session_id in memory_store:
        memory_store[session_id] = create_memory()
        return {"message": f"Memory cleared for session {session_id}"}
    
    return {"message": "Session not found"}