import json
import re
import xml.etree.ElementTree as ET

import pandas as pd  # for storing text and embeddings data
from bs4 import BeautifulSoup

from db.chroma import save_embedding_to_chroma
from db.create_embedding import create_embedding

# XMLファイルを読み込む
tree = ET.parse('db/data/Wikipedia.xml')
root = tree.getroot()

# 名前空間の取得
ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}


# ページ情報を取得する関数
def get_page_info(page):
    title = page.find('mw:title', ns).text
    text = page.find('.//mw:text', ns).text
    return title, treat_string(text)


# 正規表現を使って、{{}}と{||}のカッコと中の文字を削除し、[[]]のカッコを外す
pattern = r"\{\{.*?\}\}|\{\|\|.*?\|\|\}|\[\[(.*?)\]\]"


def treat_string(str_text):
    soup = BeautifulSoup(str_text, 'html.parser')
    str_text = soup.get_text(strip=True, separator='\n')
    str_text = remove_newlines(str_text)
    return re.sub(pattern, "", str_text)


def remove_newlines(s):
    return s.replace('\n', '')


# すべてのページのタイトルとテキストをリストに保存
pages = []
for page in root.findall('mw:page', ns):
    title, text = get_page_info(page)
    embedding = create_embedding(text)
    json_data = {
        'title': title,
        'text': text,
    }
    json_string = json.dumps(json_data)
    pages.append({'text': json_string, 'embedding': embedding})

df = pd.DataFrame(pages)
save_embedding_to_chroma(df)
