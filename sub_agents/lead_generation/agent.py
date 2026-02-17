import os
from google.adk.agents import LlmAgent
from utils.json_rules import JSON_ONLY_RULE

MODEL = os.getenv("GEN_FAST_MODEL", "gemini-2.0-flash")

lead_generation_agent = LlmAgent(
    name="LeadGenerator",
    model=MODEL,
    instruction=f"""
You generate company leads.

Output format:
{{
  "leads": [
    {{
      "company_name": "string",
      "why_match": "string",
      "target_roles": ["string"],
      "suggested_contact_method": "string",
      "confidence": 0
    }}
  ]
}}

{JSON_ONLY_RULE}
""".strip(),
)
