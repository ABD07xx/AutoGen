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

from autogen.coding import DockerCommandLineCodeExecutor


temp_dir = tempfile.TemporaryDirectory()


executor = DockerCommandLineCodeExecutor(
    image="python:3.12-slim",  
    timeout=10,  
    work_dir=temp_dir.name, 
)


code_executor_agent_using_docker = ConversableAgent(
    "code_executor_agent_docker",
    llm_config=llm_config,  
    code_execution_config={"executor": executor},  
    human_input_mode="ALWAYS",  
)


task = """
Check if this code is Correct If its incorrect save the python corrected code in a file 
Systen,out.println("Hello World)

"""
code_executor_agent_using_docker.initiate_chat(
    code_executor_agent_using_docker,
    message=task
)


