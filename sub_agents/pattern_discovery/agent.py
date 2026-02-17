import os
from google.adk.agents import LlmAgent
from utils.json_rules import JSON_ONLY_RULE

MODEL = os.getenv("GEN_FAST_MODEL", "gemini-2.0-flash")

pattern_discovery_agent = LlmAgent(
    name="PatternDiscovery",
    model=MODEL,
    instruction=f"""
You analyze hiring patterns from intent.

Output format:
{{
  "skills_keywords": ["string"],
  "common_job_titles": ["string"],
  "hiring_signals": ["string"]
}}

{JSON_ONLY_RULE}
""".strip(),
)
