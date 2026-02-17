import asyncio
import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

load_dotenv()

MODEL = os.getenv("GEN_FAST_MODEL", "gemini-2.5-flash")

APP_NAME = "TestApp"
USER_ID = "user1"
SESSION_ID = "session1"


async def main():
    agent = LlmAgent(
        name="SimpleAgent",
        model=MODEL,
        instruction="You are a helpful AI assistant."
    )

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(agent=agent, app_name=APP_NAME, session_service=session_service)

    msg = types.Content(
        role="user",
        parts=[types.Part(text="Explain AI in 2 lines.")]
    )

    for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=msg):
        if event.is_final_response() and event.content and event.content.parts:
            print("\n✅ RESPONSE:")
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
