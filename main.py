from langchain.chat_models import init_chat_model
from Tools.calculate_tool import cal_agent
from Tools.search_tool import search_agent
from Tools.weather_tool import weather_agent

from langchain.messages import AIMessage, HumanMessage, ToolMessage

model = init_chat_model("llama3.1:8b", model_provider="ollama")

tools = [cal_agent, search_agent, weather_agent]

ToolModel = model.bind_tools(tools)

user_input = input("Ask any query: ")

ai_msg = ToolModel.invoke(user_input)

print(ai_msg.tool_calls)

messages = []
messages.append(ai_msg)

# Create tool lookup
tool_dict = {
    "cal_agent": cal_agent,
    "search_agent": search_agent,
    "weather_agent": weather_agent
}


for tool_call in ai_msg.tool_calls:

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    selected_tool = tool_dict[tool_name]

    tool_result = selected_tool.invoke(tool_args)

    messages.append(
        ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"]
        )
    )

final_response = ToolModel.invoke(messages)

print(final_response.content)