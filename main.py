from src.agent.agent import Agent
from duckduckgo_search import DDGS

base_url = "http://localhost:11434/v1"
model_name = "llama3.2:3b"

system_prompt = """ 
    You are great Assistant.

    you have access to following tools:

    Search:
    e.g. search: weather temperature
    return summary from searching

    you will receive a message from human , then you should start a loop:
    You run in a chain of actions:  Thought, Action, Action Input, PAUSE, Observation
    Thought: To describe your thoughts about the question have been asked
    Action: To run one of the actions avaible to you [Search].return a  json format ( key-value pair ) like this:
            '{"action": <tool_name>}' as JSON string
    Action Input: To create input to the to action, to be send to the tool. return a json format (key-value pair) like this:
                '{"action_input" : <input_action>}' as JSON string
    
     
    Example session have this Format :
    
    Question: What is the capital of England?
    Thought: I should use tool if I am not sure about 
    Action:'{"action": "Search"}'
    Action Input: '{"action_input": "what is the captial of England"}'
    PAUSE


"""


def main():
    print("Hello from simple-local-agent!")

    # create agent
    my_agent = Agent(base_url, "empty_key", model_name, system_prompt)
    # send message to ask
    result = my_agent("what is the weather in Dallas Texas now?")
    print(result)


if __name__ == "__main__":
    main()
