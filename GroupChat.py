import autogen
from autogen import ConversableAgent

config_list = [
    {
        'model': 'gpt-4',
        'api_key':'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'
    }
]

llm_config = {
    "seed":42,
    "config_list":config_list,
    "temperature":0.4
}

number_agent = ConversableAgent(
    name = "Number Agent",
    system_message="You return me the numbers I give you, one number each line.",
    llm_config=llm_config,
    description="Return the number",
    human_input_mode="NEVER"
)
adder_agent = ConversableAgent(
    name = "Adder Agent",
    system_message="Every time add 1 to the number given to you and then return it",
    llm_config=llm_config,
    description="Add 1 to each number",
    human_input_mode="NEVER"
)
Multiply_agent = ConversableAgent(
    name = "Multiply Agent",
    system_message="Every time multiply 2 to the number given to you and then return it",
    llm_config=llm_config,
    description="Multiply 2 to each number",
    human_input_mode="NEVER"
)
subtract_agent = ConversableAgent(
    name = "Subtract Agent",
    system_message="Every time subtract 1 to the number given to you and then return it",
    llm_config=llm_config,
    description="Subtract 1 to each number",
    human_input_mode="NEVER"
)
Divide_agent = ConversableAgent(
    name = "Divide Agent",
    system_message="Every time Divide 2 to the number given to you and then return it",
    llm_config=llm_config,
    description="Divide 2 to each number",
    human_input_mode="NEVER"
)
print_agent = ConversableAgent(
    name="Print",
    system_message="You have to present the final answer along with all the calculations performed",
    llm_config=llm_config,
    description="Used for Printing and showing the process of operations",
    human_input_mode="NEVER"
)

group_chat = autogen.GroupChat(
    agents=[number_agent,adder_agent,Multiply_agent,subtract_agent,Divide_agent,print_agent],
    messages=[],
    max_round=6
)

group_chat_manager = autogen.GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)
chat_result = number_agent.initiate_chat(
    group_chat_manager,
    message="My number is 3, I want to turn it into 13.",
    summary_method="last_msg",
)
import pprint
pprint.pprint(chat_result.cost)