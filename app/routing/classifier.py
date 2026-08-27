from dataclasses import dataclass


@dataclass(frozen=True)
class Classification:
    task_type: str
    confidence: float
    reason: str


CODE_KEYWORDS = {
    "code",
    "coding",
    "program",
    "programming",
    "python",
    "javascript",
    "typescript",
    "java",
    "c++",
    "c#",
    "sql",
    "function",
    "class",
    "bug",
    "debug",
    "debugging",
    "refactor",
    "refactoring",
    "api",
    "endpoint",
    "repository",
    "repo",
    "git",
    "docker",
    "compile",
    "compiler",
    "exception",
    "stack trace",
}

VISION_KEYWORDS = {
    "image",
    "photo",
    "picture",
    "screenshot",
    "diagram",
    "visual",
    "vision",
    "ocr",
    "scan",
}

REASONING_KEYWORDS = {
    "explain",
    "analyze",
    "analysis",
    "compare",
    "reason",
    "reasoning",
    "plan",
    "planning",
    "architecture",
    "design",
    "why",
    "strategy",
    "evaluate",
    "decision",
}


def classify_task(prompt: str) -> Classification:
    text = prompt.lower()

    code_score = sum(
        1 for keyword in CODE_KEYWORDS
        if keyword in text
    )

    vision_score = sum(
        1 for keyword in VISION_KEYWORDS
        if keyword in text
    )

    reasoning_score = sum(
        1 for keyword in REASONING_KEYWORDS
        if keyword in text
    )

    scores = {
        "coding": code_score,
        "vision": vision_score,
        "reasoning": reasoning_score,
    }

    # Vision-first routing
    if vision_score > 0:
        task_type = "vision"
    else:
        task_type = max(
            scores,
            key=scores.get,
        )

    highest_score = scores[task_type]

    if highest_score == 0:
        return Classification(
            task_type="reasoning",
            confidence=0.40,
            reason="No strong task-specific keywords detected",
        )

    total = sum(scores.values())

    confidence = highest_score / total

    return Classification(
        task_type=task_type,
        confidence=round(confidence, 2),
        reason=f"Keyword scores: {scores}",
    )