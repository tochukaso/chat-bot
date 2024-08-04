"""
ChromaDB に関する処理を行うモジュール
"""
import chromadb
from chromadb.config import Settings
from config.chroma import CHROMA_DB_PATH
from util import log

settings = Settings()

chroma_client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH,
    settings=Settings(),
)


def get_embedding_collection():
    """
    wikipediaのコレクションを取得する
    :return:
    """
    return chroma_client.get_collection(name='wikipedia')


def save_embedding_to_chroma(df_embedding):
    """
    wikipediaのベクトルデータをchromadbに保存する
    :param df_embedding:
    :return:
    """
    w_collection = chroma_client.get_or_create_collection(name='wikipedia')
    # すでにデータが登録されている場合は削除する
    if w_collection.count() > 0:
        w_collection.delete(w_collection.get()['ids'])

    ids = df_embedding.index.astype(str).tolist()
    w_collection.add(
        ids=ids,
        documents=df_embedding['text'].tolist(),
        embeddings=df_embedding['embedding'].tolist(),
    )
    log.info('save_embedding_to_chroma done. collection size:', len(ids))


def detect_similarity(
        query_embedding: str,
        max_results: int = 100) -> tuple[list[str], list[float]]:
    """
    登録済みのwikipediaのベクトルデータと入力値の類似度を検出して上位N件を返す
    :param query_embedding:
    :param max_results:
    :return:
    """
    collection = get_embedding_collection()
    results = collection.query(query_embeddings=query_embedding, n_results=max_results,
                               include=['documents', 'distances'])

    strings = results['documents'][0]
    relatednesses = [1 - x for x in results['distances'][0]]
    return strings, relatednesses
