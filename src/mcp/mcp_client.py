# tools_client.py
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
import os

load_dotenv()
class McpClient:
    def __init__(self, server_url: str = os.getenv("MCP_SERVER"), server_key: str = "mcp_sever_name"):
        self.client = MultiServerMCPClient({
            server_key: {
                "url": server_url,
                "transport": "sse"
            }
        })
        self.tools_map = {}

    async def init(self):
        tools = await self.client.get_tools()
        self.tools_map = {tool.name: tool for tool in tools}
        print("this is toolsmap " , self.tools_map)

    def get_tool(self, name: str):
        if name not in self.tools_map:
            raise ValueError(f"Tool '{name}' not found. Did you run `await init()`?")
        return self.tools_map[name]

    async def invoke_tool(self, name: str, input_data: dict):
        tool = self.get_tool(name)
        return await tool.ainvoke(input_data)


# globals
tools: list = []
mcp_client: McpClient = None

async def get_mcpInstance():
    return mcp_client

async def init_tool_service():
    global mcp_client, tools
    mcp_client = McpClient()  # your SSE or HTTP client
    await mcp_client.init()
    print("initial toolmap : ",  mcp_client.tools_map)
