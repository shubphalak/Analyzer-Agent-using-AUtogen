import streamlit as st
import asyncio
import os

from team.analyzer_gemini import get_Data_Analyzer_Team
from models.models import get_model_client
from config.docker_util import get_docker_commandline_executor, start_docker_executor, stop_docker_executor
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title('Analyser GPT- Digital Data Analyzer') 

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# streamlit's variable
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None
if 'images_shown' not in st.session_state:
    st.session_state.images_shown = []

task = st.chat_input("Enter your task here...")


async def run_analyser_gpt(docker, model_client, task):
    try:
        await start_docker_executor(docker)
        team = get_Data_Analyzer_Team(docker, model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)

        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                if message.source.startswith('user'):
                    with st.chat_message('user', avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Data_Analyzer_agent'):
                    with st.chat_message('Data Analyzer', avatar='🤖'):
                        st.markdown(message.content)
                elif message.source.startswith('Python_Code_Executor'):
                    with st.chat_message('Data Analyzer', avatar='👨‍💻'):
                        st.markdown(message.content)
                st.session_state.messages.append(message.content)

            elif isinstance(message, TaskResult):
                st.markdown(f'Stop Reason : {message.stop_reason}')
                st.session_state.messages.append(message.stop_reason)

        st.session_state.autogen_team_state = await team.save_state()
        return None

    except Exception as e:
        st.error(f"Error: {e}")
        return e

    finally:
        await stop_docker_executor(docker)


async def do_something_big():
    await asyncio.sleep(1)  # Simulate a long-running task


if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

if task:
    if uploaded_file is not None: 
        if not os.path.exists('temp'):
            os.makedirs('temp', exist_ok=True)

        with open('temp/data.csv', 'wb') as f:
            f.write(uploaded_file.getbuffer())

        openai_model_client = get_model_client()   # <-- get the instance here
        docker = get_docker_commandline_executor()

        error = asyncio.run(run_analyser_gpt(docker, openai_model_client, task))  # <-- pass instance, not function

        if error:
            st.error(f'An error occured: {error}')

        if os.path.exists('temp/output.png'):
            st.image('temp/output.png')

    else:
        st.warning('Please upload the file and provide the task')

else:
    st.warning('Please provide the task')
