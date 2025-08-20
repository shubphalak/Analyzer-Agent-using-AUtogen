import asyncio
from config.docker_util import get_docker_commandline_executor , start_docker_executor, stop_docker_executor
from config.constants import work_dir, timeout
from models.models import get_model_client
from team.analyzer_gemini import get_Data_Analyzer_Team

async def main():
    docker = get_docker_commandline_executor()
    model_client = get_model_client()
    await start_docker_executor(docker)

    team = get_Data_Analyzer_Team(model_client, docker)
    print("Team created with participants:")    

    try:
        task = 'Which species has the largest average petal width? in iris.csv'

        await start_docker_executor(docker)

        async for message in team.run_stream(task=task):
            print(message)

    except Exception as e:
        print(e)
    finally:
        await stop_docker_executor(docker)


if(__name__=='__main__'):
    asyncio.run(main())