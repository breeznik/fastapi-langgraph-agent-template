from langgraph.checkpoint.memory import MemorySaver
from .state import State
from langgraph.graph import StateGraph
from . import constants
from .nodes import nodes , agents
from langgraph.graph import END


memory = MemorySaver()
graph_builder = StateGraph(State)

graph_builder.add_node(constants.SAMPLE_AGENT, agents.sample_agent)
graph_builder.add_node(constants.SAMPLE_NODE , nodes.sample_node)

graph_builder.set_entry_point(constants.SAMPLE_AGENT)
graph_builder.add_edge(constants.SAMPLE_AGENT , constants.SAMPLE_NODE)
graph_builder.add_edge(constants.SAMPLE_NODE , END)

sample_graph = graph_builder.compile(memory)
