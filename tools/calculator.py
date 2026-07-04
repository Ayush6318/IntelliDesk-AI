from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example:
    25*8
    """
    return str(eval(expression))