from langchain.tools import tool
from datetime import datetime

@tool
def current_time() -> str:
    """
    Return the current local date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(current_time.invoke({}))