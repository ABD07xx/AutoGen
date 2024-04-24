import autogen

config_list_mistral = [
    {
        "model":"mistral",
        'base_url' : "http://localhost:4000/v1",
        "api_key":"NULL"
    }
]
config_list_codellama = [
    {
        "model":"mistral",
        'base_url' : "http://localhost:43416/v1",
        "api_key":"NULL"       
    }
]

llm_config_mistral = {
    "config_list": config_list_mistral,
    "temperature":0.5
}

llm_config_codellama = {
    "config_list": config_list_codellama,
    "temperature":0.5
}

assistant = autogen.AssistantAgent(
    name="LocalAssistant",
    llm_config=llm_config_mistral

)
coder = autogen.AssistantAgent(
    name="CoderAgent",
    llm_config=llm_config_codellama,
    description="It will help you in writing codes"
)

user_proxy = autogen.UserProxyAgent(
    name = "user-proxy-1",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x:x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={'work_dir':'cwd'},
    llm_config=llm_config_mistral,
    system_message="""TERMINATE when task has been solved at full satisfaction, Otherwise Reply CONTINUE, or the reason when task isn't solved"""
)

task ="""
Write a code to print 10 prime numbers also generate 10 random coding problems in increasing order of difficulty
"""

groupchat  = autogen.GroupChat(
            agents=[user_proxy,assistant,coder],
            messages=[],
            max_round=12
)

groupchat_manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config_mistral
)

user_proxy.initiate_chat(
    groupchat_manager,
    message=task

)