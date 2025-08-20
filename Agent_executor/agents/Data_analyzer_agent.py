from autogen_agentchat.agents import AssistantAgent
from agents.Data_analyzer_msg import DATA_ANALYZER_SYSTEM_MESSAGE , sys_msg

def getdata_analyzer_agent(model_client):

    data_analyzer_agent = AssistantAgent(
        name='Data_Analyzer_Agent',
        model_client=model_client,
        description="An agent that analyzes data and writes Python code to answer user questions about CSV files.",
        system_message = sys_msg
    )
    return data_analyzer_agent