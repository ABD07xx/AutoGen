import tempfile

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

config_list =  [
    {
        'model': 'gpt-4',
        'api_key':'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'
    }
]

llm_config = {
    "seed":42, 
    "config_list": config_list,
    "temperature" :0
    }



code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=llm_config,
    code_execution_config={'work_dir':'cwd'},
    human_input_mode="TERMINATE",  
)

task = """
Check if this code is Correct If its incorrect save the python corrected code in a file 
for num in range(1, 101):
    if num % 2 = 0:
        print(num)

"""
code_executor_agent.initiate_chat(
    code_executor_agent,
    message=task
)


