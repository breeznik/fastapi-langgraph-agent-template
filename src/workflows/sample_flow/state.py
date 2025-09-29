from typing import TypedDict
from langchain_core.messages import BaseMessage


# custome state

class State(TypedDict):
    # not using annotation with add_message to reset the chat in flow.
    messages:  list[BaseMessage]
    state: dict
    