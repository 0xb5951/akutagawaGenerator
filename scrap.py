# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

target_url = "https://aozorashoin.com/author/879"

html = urllib2.urlopen(url)

# 対象の要素を再帰的にページ読み込み
# ３秒ぐらいまつ

# table table-hover配下のaタグを配列に格納
# for eachでループを回す

# ページ中のH1タグがタイトル。これを元にファイルを生成
# divのid='text'配下に本文が格納されている
# これの処理はあとで考える