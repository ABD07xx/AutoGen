import autogen

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

from autogen import ConversableAgent

student_agent = ConversableAgent(
    name="Student Agent",
    system_message="You are a student who wants to learn about Large Language Models",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

teacher_agent = ConversableAgent(
    name = "Teacher_Agent",
    system_message = "You are post doc in Large Language Models and know answer to every question",
    llm_config=llm_config,
    human_input_mode="NEVER" 
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    message="What is a Large Language Model",
    summary_method="reflection_with_llm",
    max_turns=2
)
# Get the chat history.
import pprint
pprint.pprint(chat_result.cost)