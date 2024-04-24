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

Player1 = ConversableAgent(
    "Player1",
    system_message="You are playing a game of guess-my-number. You have the "
                    "number 53 in your mind, and I will try to guess it. "
                    "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
    llm_config=llm_config,
    human_input_mode="NEVER",  
)

Player2 = ConversableAgent(
    "Player2",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config=llm_config,
    human_input_mode="NEVER",  
)

result = Player2.initiate_chat(
    Player1, 
    message="Player2, Lets play", 
    max_turns=5
    )
