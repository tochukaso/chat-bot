import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from chat.query import QueryInput, query

is_dev = os.getenv('IS_DEV', 'true')

# 開発環境であれば docs を有効に、本番環境では無効にする
docs_url = "/docs" if is_dev.lower() == 'true' else None

app = FastAPI(docs_url=docs_url, redoc_url=docs_url)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"health": "ok"}


@app.post("/chat")
def chat(query_input: QueryInput):
    return query(query_input)
