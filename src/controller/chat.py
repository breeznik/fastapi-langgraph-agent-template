# src/controllers/workflow_controller.py
from langchain_core.messages import HumanMessage
from langgraph.types import Command
from src.workflows.sample_flow.flow import sample_graph

class Chat:
    def __init__(self, message: str, checkpoint_id: str | int | None = None):
        self.message = message
        self.checkpoint_id = checkpoint_id
        self.config = {"configurable": {"thread_id": checkpoint_id}}

    async def run(self) -> str:
        snapshot = sample_graph.get_state(self.config)
        print("Snapshot:", snapshot)
        # the next would be empty if the last flow run ended that would start a new flow so to migrate the messages history using potential_messages
        potential_messages = snapshot.values.get("messages", [])
        if snapshot.next:
            print("[Workflow] Resuming graph with message:", self.message)
            result = await sample_graph.ainvoke(Command(resume=self.message), config=self.config)
        else:
            print("[Workflow] Starting new graph with message:", self.message)
            result = await sample_graph.ainvoke({"messages": potential_messages + [HumanMessage(content=self.message)]}, config=self.config)

        return result
