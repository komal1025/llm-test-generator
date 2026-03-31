def evaluate_response(response):
    score = 0
    issues = []

    if len(response) < 50:
        issues.append("Too short")
    else:
        score += 1

    if "edge" in response.lower():
        score += 1
    else:
        issues.append("No edge cases")

    if "error" in response.lower():
        score += 1
    else:
        issues.append("No error handling")

    return {
        "score": score,
        "issues": issues,
        "quality": "Good" if score >= 2 else "Weak"
    }