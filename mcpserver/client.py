from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

import asyncio

from dotenv import load_dotenv
load_dotenv()


async def main():
    client = MultiServerMCPClient(
   {
    "math":{
        "command":"python",
        "args":["mathserver.py"],
        "transport":"stdio"
    },
    "weather":{
        "url":"http://127.0.0.1:8000/mcp",
        "transport":"streamable-http", 
    }
   })


    import os

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    os.environ['ANTHROPIC_API_KEY'] = os.getenv("ANTHROPIC_API_KEY")

    tools = await client.get_tools()
    
    model = init_chat_model("claude-sonnet-4-5")

    agent = create_agent(model,tools)

    res = await agent.ainvoke({"messages":[{"role":"user","content":"what is 2+2"}]})

    print(res["messages"][-1].content)

    res = await agent.ainvoke({"messages":[{"role":"user","content":"what is the weather like in hyderabad"}]})

    print(res["messages"][-1].content)

asyncio.run(main())