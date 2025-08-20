from models import get_model_client
import asyncio
from autogen_agentchat.messages import UserMessage

import asyncio

async def main():
    client = get_model_client()
    
    response = await client.create([
        UserMessage(content="What is the capital of France?", source="user")
    ])
    
    print("Response:", response)

if __name__ == "__main__":
    asyncio.run(main())
