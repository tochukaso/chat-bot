import os

import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from config.chroma import CHROMA_DB_PATH
from config.openai import EMBEDDING_MODEL
from util import log

settings = Settings()

chroma_client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH,
    settings=Settings(),
)

embedding_function = OpenAIEmbeddingFunction(api_key=os.getenv('OPENAI_API_KEY'), model_name=EMBEDDING_MODEL)


def get_embedding_collection():
    return chroma_client.get_collection(name='wikipedia')


def save_embedding_to_chroma(df_embedding):
    log.info('save_embedding_to_chroma', df_embedding['text'].tolist())
    w_collection = chroma_client.get_or_create_collection(name='wikipedia')
    # すでにデータが登録されている場合は削除する
    w_collection.delete()
    ids = df_embedding.index.astype(str).tolist()
    w_collection.add(
        ids=ids,
        documents=df_embedding['text'].tolist(),
        embeddings=df_embedding['embedding'].tolist(),
    )
    log.info('save_embedding_to_chroma done. collection size:', len(ids))


def query_collection(
        query_embedding: str,
        max_results: int = 100) -> tuple[list[str], list[float]]:
    collection = get_embedding_collection()
    results = collection.query(query_embeddings=query_embedding, n_results=max_results,
                               include=['documents', 'distances'])

    strings = results['documents'][0]
    relatednesses = [1 - x for x in results['distances'][0]]
    return strings, relatednesses
