import os
from typing import List, Optional

from config.openai import GPT_MODEL
from openai import OpenAI
from pydantic import BaseModel

BASE_PROMPT = """
You are an intellectual who knows everything there is to know about baseball.

Please answer baseball-related questions in as much detail as possible.
"""

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


class QueryInput(BaseModel):
    message: str
    old_queries: Optional[List[str]] = None
    old_responses: Optional[List[str]] = None


class QueryOutput(BaseModel):
    reply: str


def query(query_input: QueryInput):
    chat_response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": BASE_PROMPT},
            {"role": "user", "content": query_input.message},
        ], )

    return {'reply': chat_response.choices[0].message.content}
