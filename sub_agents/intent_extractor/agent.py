import os
from google.adk.agents import LlmAgent
from utils.json_rules import JSON_ONLY_RULE

MODEL = os.getenv("GEN_FAST_MODEL", "gemini-2.0-flash")

intent_extractor = LlmAgent(
    name="IntentExtractor",
    model=MODEL,
    instruction=f"""
You convert a user request into structured JSON.

Output format:
{{
  "country": "string",
  "city": "string",
  "domain": "string",
  "role": "string",
  "count": 0,
  "must_have": ["string"],
  "nice_to_have": ["string"]
}}

{JSON_ONLY_RULE}
""".strip(),
)
