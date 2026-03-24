def analyze_logs(log_text):
    prompt = f"""
    Analyze logs and provide:
    - Root cause
    - Failure pattern
    - Suggested tests

    Logs:
    {log_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']