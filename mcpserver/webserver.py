from mcp.server.fastmcp import FastMCP

mcp =FastMCP("Weather")

@mcp.tool()
async def get_weather(city:str):
    """
    This is used to get the weather of a city
    """
    return f"Weather of {city} is sunny and temperature is 25 degrees Celsius"

if __name__ == "__main__":
    mcp.run(transport="streamable-http") 