import logging

# ログの設定を行う
logging.basicConfig(filename='gpt.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')


def info(*text: str):
    print(text)
    logging.info(text)
