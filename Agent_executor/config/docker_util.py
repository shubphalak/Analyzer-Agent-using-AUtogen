from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import work_dir, timeout

def get_docker_commandline_executor():
    docker = DockerCommandLineCodeExecutor(
        work_dir=work_dir,
        timeout=timeout
    )
    return docker

async def start_docker_executor(docker_executor):
    print("Starting Docker Command Line Code Executor...")
    await docker_executor.start()
    print("Docker Command Line Code Executor started.")

async def stop_docker_executor(docker_executor):
    print("Stopping Docker Command Line Code Executor...")
    await docker_executor.stop()
    print("Docker Command Line Code Executor stopped.")
