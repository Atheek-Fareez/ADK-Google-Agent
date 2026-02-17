import asyncio
import json
import re
from dotenv import load_dotenv

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

from sub_agents.intent_extractor.agent import intent_extractor
from sub_agents.pattern_discovery.agent import pattern_discovery_agent
from sub_agents.lead_generation.agent import lead_generation_agent

load_dotenv()

APP_NAME = "LeadGenerationResearch"
USER_ID = "local_user"
SESSION_ID = "session_1"


async def run_llm(agent, text: str, max_retries: int = 8) -> str:
    session_service = InMemorySessionService()
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)

    runner = Runner(agent=agent, app_name=APP_NAME, session_service=session_service)
    msg = types.Content(role="user", parts=[types.Part(text=text)])

    for attempt in range(1, max_retries + 1):
        try:
            final_text = ""
            for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=msg):
                if event.is_final_response() and event.content and event.content.parts:
                    final_text = (event.content.parts[0].text or "").strip()
            return final_text

        except Exception as e:
            err = repr(e)
            if "429" in err or "RESOURCE_EXHAUSTED" in err:
                m = re.search(r"retry in ([0-9]+(\.[0-9]+)?)s", err, re.IGNORECASE)
                wait_s = float(m.group(1)) if m else 30.0
                print(f"\n⏳ 429 rate limit. Waiting {wait_s:.1f}s then retrying... ({attempt}/{max_retries})")
                await asyncio.sleep(wait_s + 1)
                continue
            raise

    print("\n❌ Still rate-limited after retries.")
    return ""


def safe_json(text: str, label: str):
    if not text.strip():
        print(f"\n❌ {label} returned EMPTY output.")
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print(f"\n❌ {label} returned NON-JSON:\n{text}")
        return None


async def main():
    user_query = "Find me 2 Sri Lankan IT companies that might hire AI interns in Colombo."

    intent_text = await run_llm(intent_extractor, user_query)
    intent = safe_json(intent_text, "IntentExtractor")
    if intent is None:
        return

    patterns_text = await run_llm(pattern_discovery_agent, json.dumps(intent))
    patterns = safe_json(patterns_text, "PatternDiscovery")
    if patterns is None:
        return

    lead_input = {"intent": intent, "patterns": patterns}
    leads_text = await run_llm(lead_generation_agent, json.dumps(lead_input))
    leads = safe_json(leads_text, "LeadGenerator")
    if leads is None:
        return

    print("\n✅ LEADS:")
    print(json.dumps(leads, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
