
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.Data_analyzer_agent import getdata_analyzer_agent
from agents.Code_executor_agent import construct_code_executor_agent

def get_Data_Analyzer_Team(model_client, docker):

    code_excecutor_agent = construct_code_executor_agent(docker)
    data_analyzer_agent = getdata_analyzer_agent(model_client)
    text_mention_termination = TextMentionTermination('STOP')


    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_excecutor_agent],
        max_turns=10,
        termination_condition= text_mention_termination,
    )
    return team

