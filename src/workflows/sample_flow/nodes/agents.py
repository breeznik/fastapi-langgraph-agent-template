from langchain_core.messages import AIMessage , SystemMessage
from dotenv import load_dotenv
from src.utils.util import model_creator
from ..state import State
from .. import constants
from .. import instructions
from .. import schema
import os

load_dotenv()
global_model_key:str = os.getenv("AI_MODEL")

global_model = model_creator(global_model_key)
local_model = model_creator(constants.AIModels.GPT_4O_MINI)
pinky_saver = model_creator(constants.AIModels.XAI_CODE_FAST)

async def sample_agent(state:State):
    messages = state.get("messages",[])
    sm = SystemMessage(instructions.sample_instruction.format())
    structured_llm = global_model.with_structured_output(schema.sample_schema)
    try:
        response:schema.sample_schema = structured_llm.invoke(messages + [sm])
        ai_message = AIMessage(content=response.message)
        messages.append(ai_message)
    except Exception as error:
        # handle the error here
        print("An Error Occured" , error)
        sm = SystemMessage(content="There was error an during ai call , please try again.")
        messages.append(sm)
        
    return {"messags": messages}