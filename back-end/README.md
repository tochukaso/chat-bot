# Back end

## General Requirement

- Python 3.12.4
    - [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)

# How to install

Pythonのプロジェクトの初期化

```bash
python3.12 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Pythonのサーバープログラムを実行するためのパッケージのインストール

```sh
pip3 install "uvicorn[standard]"
```


# How to run

以下のコマンドでアプリケーションを立ち上げることが出来ます。

```sh
uvicorn server:app --reload --port 4000\
```

http://localhost:4000/docs にアクセスすると、Swagger UIが表示されます。

# How to create vector data

Open AIの embedding を使って、事前にWikipedia情報をベクトルデータとして保存します。

```sh
python3 create_index.py
```
