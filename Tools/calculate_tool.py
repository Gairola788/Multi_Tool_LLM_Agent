from langchain.tools import tool


@tool
def cal_agent(expression : str) -> str:
    """Calculate the expression including addition,subtraction,multiplication and Division,
         args : any expression for example : 5 + 3
         
          Args:
        expression: A mathematical expression, for example '5 + 3' or '3000 + 2500 + 4000'
    
         Returns:
        The calculated result"""
    try:
        result = eval(expression)
        return f"Result: {result}"

    except:
        return "Invalid mathematical expression."
    