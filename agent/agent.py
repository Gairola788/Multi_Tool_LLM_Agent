from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import streamlit as st

from langchain.messages import (
    HumanMessage,
    ToolMessage,
    SystemMessage
)

from Tools.calculate_tool import cal_agent
from Tools.search_tool import search_agent
from Tools.weather_tool import weather_agent

# ------------------ LOAD ENV ------------------

load_dotenv()

# ------------------ MODEL ------------------

model = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model_name="llama-3.1-8b-instant"
)

# ------------------ TOOLS ------------------

tools = [cal_agent, search_agent, weather_agent]

ToolModel = model.bind_tools(tools)

tool_dict = {
    "cal_agent": cal_agent,
    "search_agent": search_agent,
    "weather_agent": weather_agent
}

# ------------------ SYSTEM PROMPT ------------------

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Use tools ONLY when necessary.

Rules:
- Use calculator tool ONLY for math calculations.
- Use weather tool ONLY for weather-related queries.
- Use search tool ONLY for current events or internet-based information.
- For general programming or educational questions, answer directly without tools.
"""

# ------------------ MEMORY ------------------

def create_memory():

    return [
        SystemMessage(content=SYSTEM_PROMPT)
    ]

# ------------------ MEMORY TRIM ------------------

def trim_memory(messages: list, limit: int = 10):

    if len(messages) > limit:
        return [messages[0]] + messages[-limit:]

    return messages

# ------------------ CORE AGENT ------------------

def run_agent(user_input: str, messages: list):

    # Add user message
    messages.append(HumanMessage(content=user_input))

    # First LLM call
    ai_msg = ToolModel.invoke(messages)

    messages.append(ai_msg)

    # ------------------ NO TOOL CASE ------------------

    if not ai_msg.tool_calls:

        if ai_msg.content:
            return ai_msg.content, messages

        return "⚠️ No response generated.", messages

    # ------------------ TOOL CASE ------------------

    results = []

    for tool_call in ai_msg.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        print(f"[TOOL USED]: {tool_name}")

        selected_tool = tool_dict.get(tool_name)

        # Safety check
        if not selected_tool:
            tool_result = f"Tool '{tool_name}' not found"

        else:
            try:
                tool_result = selected_tool.invoke(tool_args)

            except Exception as e:
                tool_result = f"Error: {str(e)}"

        # Save tool output into memory
        messages.append(
            ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"]
            )
        )

        # ------------------ SMART ROUTING ------------------

        # ✅ Calculator
        if tool_name == "cal_agent":

            results.append(f"🧮 {tool_result}")

        # ✅ Weather
        elif tool_name == "weather_agent":

         if isinstance(tool_result, dict):

          results.append(f"""
🌤 Weather in {tool_result.get('city', 'Unknown')}

🌡 Temperature: {tool_result.get('temp', 'N/A')}°C

☁️ Condition: {tool_result.get('description', 'N/A')}

💧 Humidity: {tool_result.get('humidity', 'N/A')}%

🌬 Wind Speed: {tool_result.get('wind_speed', 'N/A')} m/s
""")

         else:

          results.append(f"⚠️ {tool_result}")

        # ✅ Search
        elif tool_name == "search_agent":

            # Use second LLM call ONLY here
            final_response = ToolModel.invoke(messages)

            messages.append(final_response)

            return final_response.content, messages

        # fallback
        else:
            results.append(str(tool_result))

    return "\n".join(results), messages