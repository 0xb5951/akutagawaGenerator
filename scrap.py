# coding: UTF-8
import re
import requests
from bs4 import BeautifulSoup

target_url = "https://aozorashoin.com/author/879"

r = requests.get(target_url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(r.text, "html.parser")

# table table-hover配下のaタグを配列に格納
author_page_a_tag = soup.find('table', class_="table-hover").find_all('a', href=re.compile('../title/.*'))

for a_tag in author_page_a_tag:
    book_links = a_tag.get('href').strip('..')

# 対象の文書リンクを配列の長さだけループ

# ページ中のH1タグがタイトル。これを元にファイルを生成
# divのid='text'配下に本文が格納されている
# 本文へのリンクは`title/X'となっている
# これの処理はあとで考える