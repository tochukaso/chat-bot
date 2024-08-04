"""
Utility functions.
"""
import tiktoken

from config.openai import GPT_MODEL


def count_tokens(text: str, model: str = GPT_MODEL) -> int:
    """Return the number of tokens in a string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))
