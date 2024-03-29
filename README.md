## 概要
芥川龍之介の作品情報を元に、LSTM+RNNを用いて、それっぽい文章を自動生成させる。
以前は、作品一覧を公開されていたサイトがあったが、サーバ代を支払い忘れたらしいので、
青空文庫からスクレイピングしてテキストデータを取得してくる。




## コードの実行に関して
venvで仮想環境を作成して、requirements.txtをインストールする.
まずはスクレイピングを実行。
https://aozorashoin.com/author/879


1. preprocess.py
2. lstm_rnn.py
3. textGenerator.py

前処理の段階で書籍の本文を一つのテキストファイルにまとめてしまっているため、
実行時にメモリエラーが出る可能性がある。
ので、前処理したテキストファイルを分割して、入力するなどの工夫をしてください。


## 参考文献
- このプログラムはアリス・イン・ワンダーランド（英語版）をディープラーニングで学習させ、その学習データを元に文章の生成を行います。
https://colab.research.google.com/drive/18hpMf8-lAPr9WCedHZmRXfe1h1TuAZRb#scrollTo=FO0ZwyfjlBC1

- 夏目漱石っぽい文章を作成してくれる
https://blog.aidemy.net/entry/2018/10/05/195404

- 【エヴァンゲリオン】アスカっぽいセリフをDeepLearningで自動生成してみる
https://qiita.com/S346/items/24e875e3c5ac58f55810

- Pythonリハビリのために文章自動生成プログラムを作ってみた
http://o-tomox.hatenablog.com/entry/2014/11/14/190632

- マルコフ連鎖による文章の自動生成
https://blog.kentarok.org/entry/20040415/1081998210

- LSTMで夏目漱石ぽい文章の生成
https://qiita.com/elm200/items/6f84d3a42eebe6c47caa

- Deep Learningで遊ぶ(3): LSTM-RNNで夏目漱石っぽい文章の生成にトライしてみる
https://tjo.hatenablog.com/entry/2016/11/08/190000

- RNNを使った文章の自動生成
https://www.pytry3g.com/entry/2018/03/16/203414

- ディープラーニングで文章を自動生成したい！
https://blog.aidemy.net/entry/2018/10/05/195404
