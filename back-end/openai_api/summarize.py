"""
OpenAIのchatを使用して、テキストを要約する
"""
import os

from openai import OpenAI
from config.openai import GPT_MODEL

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

SUMMARIZE_PROMPT = """
Summarize text. The summarized text will be registered as vector data using embedding, so try to include keywords in the summary.

If HTML tags or unnecessary decorative symbols are included, do not include them in the summary.
"""


def summarize(text: str) -> str:
    """
    OpenAI APIを使用して、テキストを要約する
    :param text:
    :return:
    """
    chat_response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": SUMMARIZE_PROMPT},
            {"role": "user", "content": text},
        ], )
    return chat_response.choices[0].message.content

