"""
ログ出力を行うモジュール
"""
import logging

# ログの設定を行う
logging.basicConfig(filename='gpt.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')


def info(*text: str):
    """
    標準出力とログファイルにログを出力する
    :param text:
    :return:
    """
    print(text)
    logging.info(text)
