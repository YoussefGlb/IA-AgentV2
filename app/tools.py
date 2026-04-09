from langchain.tools import Tool
from langchain.tools.python.tool import PythonREPLTool
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.tools.tavily_search import TavilySearchResults

def calculator(input: str):
    return str(eval(input))

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Performs math calculations"
    ),
    DuckDuckGoSearchRun(),
    TavilySearchResults(),
    PythonREPLTool()
]