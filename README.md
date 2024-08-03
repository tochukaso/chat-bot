# chat-bot

このプロジェクトは、RAGの精度向上を実験するためのサンプルアプリケーションです。

Wikipeadiaの情報を元にRAGの精度向上方法を検討します。

## General Requirement

- [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)
- [Node.js](https://nodejs.org/) (v18.16.0 以上推奨)
- [npm](https://www.npmjs.com/) (v9.5.1 以上推奨)

# 検証結果

## RAGを使わずに単純に質問した場合

![no rag](/images/no_rag.png)

## RAGを使って参考情報を追加して質問した場合

![rag_1](/images/rag_1.png)

1998年の夏の決勝戦のことを解説しています。

PL学園帯横浜延長17回 というタイトルの記事が最も類似度が高かったのですが、それでも **.0203** と非常に低い値でした。

ここからはRAGの精度を向上するためにできることをやっていきます。

## Front end

### 起動方法

front-end ディレクトリに移動して、以下のコマンドを実行してください。

``` sh
npm start
```

Front end は [http://localhost:3000](http://localhost:3000) でアクセスできます。

README は [こちら](front-end/README.md)

## Back end

README は [こちら](back-end/README.md)
