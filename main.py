from langchain.chat_models import init_chat_model
from langchain.tools import tool
from Tools.calculate_tool import cal_agent
from Tools.search_tool import search_agent
from Tools.weather_tool import weather_agent

from langchain.messages import AIMessage,HumanMessage,SystemMessage

model = init_chat_model("llama3.2-vision", model_provider="ollama")

tools = [cal_agent,search_agent,weather_agent]

ToolModel = model.bind_tools(tools)

user_input = input("Ask any query:")
ai_msg = ToolModel.invoke(user_input)


