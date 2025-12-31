def build_recruiter_prompt(drawbacks: list, improvements: list, score: int) -> str:
    d = "\n".join([f"- {x}" for x in drawbacks])
    i = "\n".join([f"- {x}" for x in improvements])

    return f"""
You are a senior technical recruiter.

GitHub Score: {score}/100

Confirmed Profile Drawbacks:
{d}

Planned Improvements:
{i}

TASK:
Explain how these issues affect recruiter shortlisting
and what changes would make this profile more attractive.

RULES:
- Do NOT restate the drawbacks
- Do NOT give generic GitHub advice
- Focus only on recruiter evaluation
- Output 4–6 concise bullet points
"""
