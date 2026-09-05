import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

code = """
def divide(a, b):
    return a / b
"""

prompt = f"""
You are a senior software engineer performing an automated code review.

Review the following Python code.

Look for:
1. Bugs
2. Missing error handling
3. Security problems
4. Edge cases
5. Missing tests
6. Maintainability problems

Code:

{code}

Give a concise review.
For each problem, give:
- Severity: Critical, High, Medium, or Low
- Problem
- Recommendation

At the end give:
DECISION: PASS
or
DECISION: FAIL
"""

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)

print(response.choices[0].message.content)
