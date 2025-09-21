# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: str, b: str) -> int:
    """Add two numbers"""
    return int(a) + int(b)


@mcp.tool()
def multiply(a: str, b: str) -> int:
    """Multiply two numbers"""
    return int(a) * int(b)


if __name__ == "__main__":
    mcp.run(transport="stdio")
