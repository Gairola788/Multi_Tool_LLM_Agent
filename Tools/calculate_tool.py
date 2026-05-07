from langchain.tools import tool
import math

@tool
def cal_agent(expression: str):
    """Calculate a mathematical expression like '5 + 3' or '10 * 2'."""

    print("Expression received:", expression)

    try:
        # ❗ Safe eval (restricted environment)
        result = eval(
            expression,
            {"__builtins__": None},  # block dangerous functions
            math.__dict__            # allow math functions if needed
        )

        return result   # ✅ return RAW result (important)

    except Exception:
        return {"error": "Invalid mathematical expression"}