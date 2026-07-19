import re


def clean_response(text: str) -> str:
    """
    Remove model reasoning traces.
    """

    # Remove <think>...</think> blocks
    text = re.sub(
        r"<think>.*?</think>",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove Reasoning sections
    text = re.sub(
        r"Reasoning:.*?(?=Answer:|$)",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Remove Answer: prefix
    text = re.sub(
        r"^Answer:\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    return text.strip()