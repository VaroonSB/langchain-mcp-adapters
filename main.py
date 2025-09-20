import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=[
        "/Users/varoon.balachandar/Documents/Study/AI/mcp-servers/langchain-mcp-adapters-practice/servers/math_server.py"
    ],
)


async def main():
    print("Hello from langchain-mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())
