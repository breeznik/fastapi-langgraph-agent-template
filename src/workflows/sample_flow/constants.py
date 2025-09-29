from enum import Enum

# nodes
SAMPLE_NODE = "SAMPLE_NODE"

# agents
SAMPLE_AGENT = "SAMPLE_AGENT"


# enum
class AIModels(str, Enum):
    GPT_4O = "openai/gpt-4o"
    GPT_4O_MINI = "openai/gpt-4o-mini"
    XAI_CODE_FAST = "x-ai/grok-code-fast-1"