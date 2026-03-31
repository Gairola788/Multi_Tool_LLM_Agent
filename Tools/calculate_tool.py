from langchain.tools import tool


@tool("Calculator")
def cal_agent(expression) -> str:
    """"Calculate the expression including addition,subtraction,multiplication and Division,
         args : any expression for example : 5 + 3"""
    try:
        result = eval(expression)
        return f"Result: {result}"

    except:
        return "Invalid mathematical expression."
    