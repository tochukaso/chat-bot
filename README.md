# chat-bot

このプロジェクトは、RAGの精度向上を実験するためのサンプルアプリケーションです。

Wikipediaの情報を元にRAGの精度向上方法を検討します。

<details>
<summary>Wikipediaデータ</summary>

Wikipediaのデータダンプを取得したところ、圧縮状態で3.7GB,解凍後は15.8GBとなり、ローカル環境ではデータを扱うのが難しいため、
野球に関連する[データを個別取得](https://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E3%83%87%E3%83%BC%E3%82%BF%E6%9B%B8%E3%81%8D%E5%87%BA%E3%81%97)しました。

取得したデータは12MBほどで、プロ野球、メジャーリーグ、WBC、甲子園、など野球に関連する内容から、神話、土地情報、歴史、など様々な情報が含まれています。

</details>

## General Requirement

- [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)
- [Node.js](https://nodejs.org/) (v18.16.0 以上推奨)
- [npm](https://www.npmjs.com/) (v9.5.1 以上推奨)

# 検証結果

検証に使用したAPI

- GPT-4o mini
- text-embedding-3-large

1999年の夏の甲子園の決勝戦について解説してもらいます。

[1999年の夏の甲子園](https://ja.wikipedia.org/wiki/%E7%AC%AC81%E5%9B%9E%E5%85%A8%E5%9B%BD%E9%AB%98%E7%AD%89%E5%AD%A6%E6%A0%A1%E9%87%8E%E7%90%83%E9%81%B8%E6%89%8B%E6%A8%A9%E5%A4%A7%E4%BC%9A)の決勝戦は 8/21 岡山理大付属高校　対 桐生第一高校です。

試合は 1 - 14 で桐生第一高校が勝利しました。
甲子園のキャッチフレーズは「君がいる甲子園が好き」らしいです。

## RAGを使わずに単純に質問した場合

![no rag](/images/no_rag.png)
1998年の夏の甲子園の解説と思わせながら、架空の結果を出力しています。

## RAGを使って参考情報を追加して質問した場合

![rag_1](/images/rag_1.png)

1998年の夏の決勝戦のことを解説しています。

PL学園帯横浜延長17回 というタイトルの記事が最も類似度が高かったのですが、それでも **.0203** と非常に低い値でした。

ここからはRAGの精度を向上するためにできることをやっていきます。

## Wikipediaの情報を要約したものをベクトルデータにしてRAGを構築した場合



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
