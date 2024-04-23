import autogen

config_list =  [
    {
        'model': 'gpt-4',
        'api_key':'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'
    }
]

llm_config = {
    "seed":42,  #Seed is used for caching purpose
    "config_list": config_list,
    "temperature" :0
    }

assistant = autogen.AssistantAgent(
    name = "FirstAgent",
    llm_config=llm_config
)

#UserProxy: Agent that acts on behalf of User It can perform actions Like Executing Code it can do it on its own or ask for approval to do this

user_proxy = autogen.UserProxyAgent(
    name = "user-proxy-1",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x:x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={'work_dir':'cwd'},
    llm_config=llm_config,
    system_message="""TERMINATE when task has been solved at full satisfaction, Otherwise Reply CONTINUE, or the reason when task isn't solved"""
)

task = """
Write a python code to print even numbers between 1 to 100Too
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)