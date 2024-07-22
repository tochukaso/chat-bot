import os

from openai import OpenAI
from config.openai import EMBEDDING_MODEL, EMBEDDING_MAX_TOKENS
from util.utils import count_tokens

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


def create_embedding(text):
    tokens = count_tokens(text)
    if tokens > EMBEDDING_MAX_TOKENS:
        # 8192トークンに収まるように文字列を切り詰める
        text = text[:EMBEDDING_MAX_TOKENS]

    embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return embedding_response.data[0].embedding
