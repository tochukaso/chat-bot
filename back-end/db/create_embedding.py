import os

from openai import OpenAI
from config.openai import EMBEDDING_MODEL, EMBEDDING_MAX_TOKENS
from util.utils import count_tokens

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


def create_embedding(text):
    # トークン数が8192に収まるまでループ処理する
    while True:
        tokens = count_tokens(text, EMBEDDING_MODEL)
        if tokens <= EMBEDDING_MAX_TOKENS:
            break
        # 8192トークンに収まるように文字列を切り詰める
        text = text[:min(len(text) - 100, int(EMBEDDING_MAX_TOKENS/3))]

    embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return embedding_response.data[0].embedding
