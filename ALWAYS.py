api_key = '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'

config_list = [
    {
        "model": "gpt-4",  
        "api_key": api_key
    }
]

llm_config = {
    "seed":42,  #Seed is used for caching purpose
    "config_list": config_list,
    "temperature" :0.5
    }

import os
from autogen import ConversableAgent

Player2 = ConversableAgent(
    "Player2",
    system_message="You have a number in my mind, and I will try to guess it. "
    "If I say a number greater than your number you say 'too high', If I say a number greater than your number you say 'too low', "
    "At the end if I am unable to guess you give me the number",
    llm_config=llm_config,
    human_input_mode="ALWAYS",  
)

result = Player2.initiate_chat(
    Player2,
    message="Player2, Lets play", 
    max_turns=10
    )
