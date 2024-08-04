"""
chromadbにwikipediaのベクトルデータを保存します
"""

import json
import re
import xml.etree.ElementTree as ET

import pandas as pd  # for storing text and embeddings data
from bs4 import BeautifulSoup

from db.chroma import save_embedding_to_chroma
from openai_api.embedding import embedding
from openai_api.summarize import summarize
from util import log

# XMLファイルを読み込む
tree = ET.parse('db/data/Wikipedia.xml')
root = tree.getroot()

# 名前空間の取得
ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}



# ページ情報を取得する関数
def __get_page_info(page_info):
    page_title = page_info.find('mw:title', ns).text
    page_text = page_info.find('.//mw:text', ns).text
    return page_title, __treat_string(page_text)


# 正規表現を使って、{{}}と{||}のカッコと中の文字を削除し、[[]]のカッコを外す
PATTERN = r"\{\{.*?\}\}|\{\|\|.*?\|\|\}|\[\[(.*?)\]\]"


def __treat_string(str_text):
    soup = BeautifulSoup(str_text, 'html.parser')
    str_text = soup.get_text(strip=True, separator='\n')
    str_text = __remove_newlines(str_text)
    return re.sub(PATTERN, "", str_text)


def __remove_newlines(str_text):
    return str_text.replace('\n', '')


# すべてのページのタイトルとテキストをリストに保存
pages = []
for page in root.findall('mw:page', ns):
    title, text = __get_page_info(page)
    summarized_text = summarize(text)
    log.info(f"processing [{title}], [{summarized_text}].")

    embedded = embedding(summarized_text)
    json_data = {
        'title': title,
        'text': text,
        'summary': summarized_text,
    }
    json_string = json.dumps(json_data, ensure_ascii=False, separators=(',', ':'))
    pages.append({'text': json_string, 'embedding': embedded})

df = pd.DataFrame(pages)
save_embedding_to_chroma(df)
