# coding: UTF-8
import requests
from bs4 import BeautifulSoup

target_url = "https://aozorashoin.com/author/879"

r = requests.get(target_url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(r.text, "html.parser")

# table table-hover配下のaタグを配列に格納
print(soup.find('table', class_="table-hover").a)
# for eachでループを回す

# ページ中のH1タグがタイトル。これを元にファイルを生成
# divのid='text'配下に本文が格納されている
# これの処理はあとで考える