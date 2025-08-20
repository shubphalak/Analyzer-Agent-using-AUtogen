import streamlit as st
import asyncio
import os

from config.docker_util import get_docker_commandline_executor , start_docker_executor, stop_docker_executor
from config.constants import work_dir, timeout
from models.models import get_model_client
from team.analyzer_gemini import get_Data_Analyzer_Team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title('Analyser GPT- Digital Data Analyzer') 

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])



task = st.chat_input("Enter your task here...")


async def run_analyser_gpt(docker, model_client, task):
    try:
        await start_docker_executor(docker)
        team = get_Data_Analyzer_Team(model_client , docker)

        async for message in team.run_stream(task=task):
            st.markdown(f"**{message}")
    
    except Exception as e:
        st.error(f"Error: {e}")
        return e

    finally:
        await stop_docker_executor(docker)


if task:
    if uploaded_file is not None and task:
        
        if not os.path.exists('temp'):
            os.makedirs('temp')

        with open('temp/data.csv', 'wb') as f:
            f.write(uploaded_file.getbuffer())

        model_client = get_model_client()
        docker = get_docker_commandline_executor()

        error = asyncio.run(run_analyser_gpt(docker ,model_client, task))

        if error:
            st.error(f"An error occurred: {error}")
       

    else:
        st.warning("Please upload a CSV file and enter a task.")

else:
    st.warning("Please enter a task to analyze the data.")

