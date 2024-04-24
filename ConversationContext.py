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
    human_input_mode="NEVER"
)
adder_agent = ConversableAgent(
    name = "Adder Agent",
    system_message="Every time add 1 to the number given to you and then return it",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
Multiply_agent = ConversableAgent(
    name = "Multiply Agent",
    system_message="Every time multiply 2 to the number given to you and then return it",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
subtract_agent = ConversableAgent(
    name = "Subtract Agent",
    system_message="Every time subtract 1 to the number given to you and then return it",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
Divide_agent = ConversableAgent(
    name = "Divide Agent",
    system_message="Every time Divide 2 to the number given to you and then return it",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
print_agent = ConversableAgent(
    name="Print",
    system_message="You have to present the final answer along with all the calculations performed",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
chat_results = number_agent.initiate_chats(
    [
        {
            "recipient": adder_agent,
            "message": "14",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": Multiply_agent,
            "message": "These are my numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": subtract_agent,
            "message": "These are my numbers",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": Divide_agent,
            "message": "These are my numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": print_agent,
            "message": "Printing the Numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        }
    ]
)
