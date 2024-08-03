import os
import json
from typing import List, Optional

from config.openai import GPT_MODEL, EMBEDDING_MODEL
from openai import OpenAI
from pydantic import BaseModel
from openai_api.embedding import embedding
from db.chroma import query_collection
from util import log

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
    rag_info = __exec_rag(query_input)
    prompt = BASE_PROMPT
    if rag_info:
        prompt = add_rag_info(BASE_PROMPT, rag_info)

    return __call_openapi_query(query_input, prompt)

def __exec_rag(query_input):
    embedded = embedding(query_input.message)
    strings, relatednesses = query_collection(query_embedding=embedded, max_results=10)

    rag_jsons = []
    for string, relatedness in zip(strings, relatednesses):
        log.info(relatedness, string)
        data = json.loads(string)
        extracted = {
            'title': data['title'],
            'text': data['text'],
        }

        json_string = json.dumps(extracted, ensure_ascii=False, separators=(',', ':'))
        rag_jsons.append(json_string)

    return ",".join(rag_jsons)


def add_rag_info(prompt, race_string: str):
    if race_string:
        # race_stringはJSON形式の文字列だが、配列形式となっていないため、[]で囲む
        prompt += f"""
The baseball information is JSON in the following triple quotes.
```
[{race_string}]
```
"""
    return prompt

def __call_openapi_query(query_input, prompt):
    chat_response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query_input.message},
        ], )
    return {'reply': chat_response.choices[0].message.content}

