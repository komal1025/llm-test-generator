from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(requirement):
    prompt = f"""
    Generate structured test cases in JSON format.

    Requirement:
    {requirement}

    Output format:
    [
      {{
        "test_name": "",
        "steps": [],
        "expected_result": "",
        "priority": "High/Medium/Low"
      }}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw_output": content}