from mcp.server.fastmcp import FastMCP

mcp =FastMCP("Math")

@mcp.tool()
def add(int_a:int,int_b:int):
    """
    This is used to add two numbers
    """
    return int_a+int_b

@mcp.tool()
def substract(int_a:int,int_b:int):
    """
    This is used to substract two numbers
    """
    return int_a-int_b

@mcp.tool()
def multiply(int_a:int,int_b:int):
    """
    This is used to multiply two numbers
    """
    return int_a*int_b

@mcp.tool()
def divide(int_a:int,int_b:int):
    """
    This is used to divide two numbers
    """
    return int_a/int_b

@mcp.tool()
def power(int_a:int,int_b:int):
    """
    This is used to find the power of a number
    """
    return int_a**int_b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    