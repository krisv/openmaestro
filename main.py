import asyncio

from app.agent.maestro import Maestro

async def main():
    try:
        agent = Maestro()
        prompt = input("What is your question? ")
        print(f"Start processing {prompt}")
        await agent.run(prompt)
        print(f"Done processing {prompt}")
    except KeyboardInterrupt:
        print(f"Operation interrupted.")


if __name__ == "__main__":
    asyncio.run(main())