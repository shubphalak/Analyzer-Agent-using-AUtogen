from autogen_agentchat.agents import CodeExecutorAgent
import asyncio
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

def construct_code_executor_agent(code_executor):
    code_executor_agent = CodeExecutorAgent(
        name='Python_Code_Executor',
        code_executor=code_executor
    )

    return code_executor_agent
      
