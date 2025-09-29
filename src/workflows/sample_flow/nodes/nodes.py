from ..state import State
from langchain_core.messages import SystemMessage

def sample_node(state:State) -> State:
    messages = state["messages"]
    sm = SystemMessage(content="sample node executed")
    messages.append(sm)
    return{"messages":messages}