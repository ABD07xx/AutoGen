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
    "temperature":0.5
}

English_Agent = ConversableAgent(
    name="English",
    system_message="Urdu Agent will ask you a question in Urdu you should respond in English",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
Urdu_Agent = ConversableAgent(
    name="Urdu",
    system_message="You will receive a sentece from EnglishAgent in English you've to convert it to Urdu write it in english example How are you will be aap kaise ho all sentences from your side should be in this format only",
    llm_config=llm_config,
    human_input_mode="ALWAYS"
)

English_Agent.initiate_chat(
    Urdu_Agent,
    message="Hello, How are you",
    summary_method='last_msg',
    max_turns=6
)