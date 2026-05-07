from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, ToolMessage

from Tools.calculate_tool import cal_agent
from Tools.search_tool import search_agent
from Tools.weather_tool import weather_agent

# ------------------ INIT ------------------

model = init_chat_model("mistral", model_provider="ollama")

tools = [cal_agent, search_agent, weather_agent]
ToolModel = model.bind_tools(tools)

# 🔥 Warm-up (avoids first-call delay)
try:
    ToolModel.invoke("Hello")
except:
    pass

tool_dict = {
    "cal_agent": cal_agent,
    "search_agent": search_agent,
    "weather_agent": weather_agent
}

# ------------------ CORE FUNCTION ------------------

def run_agent(user_input: str, messages: list):
    """
    Runs agent for a single query.

    Args:
        user_input (str): user query
        messages (list): conversation history

    Returns:
        response (str), updated_messages (list)
    """

    # Add user message
    messages.append(HumanMessage(content=user_input))

    # First LLM call
    ai_msg = ToolModel.invoke(messages)
    messages.append(ai_msg)

    # If tool calls exist
    if ai_msg.tool_calls:
        results = []

        for tool_call in ai_msg.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"[TOOL USED]: {tool_name}")

            selected_tool = tool_dict.get(tool_name)

            # Safety check
            if not selected_tool:
                tool_result = {"error": f"Tool '{tool_name}' not found"}
            else:
                try:
                    tool_result = selected_tool.invoke(tool_args)
                except Exception as e:
                    tool_result = {"error": str(e)}

            # Store tool response in memory
            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )

            # ------------------ SMART ROUTING ------------------

            # ✅ CALCULATOR → FAST PATH (no LLM)
            if tool_name == "cal_agent":
                if isinstance(tool_result, dict) and "error" in tool_result:
                    results.append(f"⚠️ {tool_result['error']}")
                else:
                    results.append(f"Result: {tool_result}")

            # ✅ WEATHER → FORMATTED RESPONSE
            elif tool_name == "weather_agent":
                if isinstance(tool_result, dict) and "error" in tool_result:
                    results.append(f"⚠️ {tool_result['error']}")
                else:
                    results.append(f"""🌤 Weather in {tool_result.get('city', '')}:

Temperature: {tool_result.get('temp', 'N/A')}°C
Condition: {tool_result.get('description', 'N/A')}
Humidity: {tool_result.get('humidity', 'N/A')}%
Wind Speed: {tool_result.get('wind_speed', 'N/A')} m/s
""")

            # ❌ SEARCH → USE LLM FOR BETTER RESPONSE
            elif tool_name == "search_agent":
                if isinstance(tool_result, dict) and "error" in tool_result:
                    results.append(f"⚠️ {tool_result['error']}")
                else:
                    final_response = ToolModel.invoke(messages)
                    messages.append(final_response)
                    return final_response.content, messages

            # fallback
            else:
                results.append(str(tool_result))

        # Return combined results (handles multi-tool)
        return "\n".join(results), messages

    else:
    # ✅ Case 1: Normal LLM response
     if ai_msg.content and "[TOOL_CALLS]" not in ai_msg.content:
        return ai_msg.content, messages

    # 🔄 Case 2: Fallback to search tool
    try:
        print("[FALLBACK] Using search_agent")

        tool_result = search_agent.invoke({"query": user_input})

        if isinstance(tool_result, dict) and "error" in tool_result:
            return f"⚠️ {tool_result['error']}", messages

        return f"""🔎 Answer:

{tool_result.get('result', 'No result found')}
""", messages

    except Exception as e:
        return f"⚠️ Error: {str(e)}", messages


# ------------------ MEMORY HELPERS ------------------

def create_memory():
    return []


def trim_memory(messages: list, limit: int = 10):
    if len(messages) > limit:
        return messages[-limit:]
    return messages


# ------------------ CORE FUNCTION ------------------

# def run_agent(user_input: str, messages: list):
#     """
#     Runs agent for a single query.

#     Args:
#         user_input (str): user query
#         messages (list): conversation history

#     Returns:
#         response (str), updated_messages (list)
#     """

#     # Add user message
#     messages.append(HumanMessage(content=user_input))

#     # First LLM call
#     ai_msg = ToolModel.invoke(messages)
#     messages.append(ai_msg)

#     # If tool calls exist
#     if ai_msg.tool_calls:
#         for tool_call in ai_msg.tool_calls:
#             tool_name = tool_call["name"]
#             tool_args = tool_call["args"]

#             print(f"[TOOL USED]: {tool_name}")

#             selected_tool = tool_dict.get(tool_name)

#             # Safety check
#             if not selected_tool:
#                 tool_result = f"Error: Tool '{tool_name}' not found"
#             else:
#                 try:
#                     tool_result = selected_tool.invoke(tool_args)
#                 except Exception as e:
#                     tool_result = f"Error: {str(e)}"

#             messages.append(
#                 ToolMessage(
#                     content=str(tool_result),
#                     tool_call_id=tool_call["id"]
#                 )
#             )

#         # Final LLM call
#         final_response = ToolModel.invoke(messages)
#         messages.append(final_response)

#         return final_response.content, messages

#     else:
#         return ai_msg.content, messages


# # ------------------ HELPER (OPTIONAL) ------------------

# def create_memory():
#     """Creates a fresh conversation memory"""
#     return []


# def trim_memory(messages: list, limit: int = 10):
#     """Keeps only last N messages (prevents overflow)"""
#     if len(messages) > limit:
#         return messages[-limit:]
#     return messages