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
    command="/Users/varoon.balachandar/Documents/Study/AI/mcp-servers/langchain-mcp-adapters-practice/.venv/bin/python",
    args=[
        "/Users/varoon.balachandar/Documents/Study/AI/mcp-servers/langchain-mcp-adapters-practice/servers/math_server.py"
    ],
)


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)

            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 54 + 2 * 3?")]}
            )
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
