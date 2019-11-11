# coding: UTF-8
import re
import requests
from bs4 import BeautifulSoup
import time

site_url = "https://aozorashoin.com"
auther_url = "https://aozorashoin.com/author/879"

r = requests.get(auther_url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(r.text, "html.parser")

# table table-hover配下のaタグを配列に格納
author_page_a_tag = soup.find('table', class_="table-hover").find_all('a', href=re.compile('../title/.*'))

def book_detail(book_link):
    rb = requests.get(site_url + book_link)
    book = BeautifulSoup(rb.text, "html.parser")
    print()
    title = book.h1.text
    print(title)
    with open('./source/'+title+'.txt', mode='x') as f:
        f.write(str(book.select("#text")))
    time.sleep(5)
    return

book_links = [] 
for a_tag in author_page_a_tag:
    book_links.append(str(a_tag.get('href').replace('..', '')))

print(book_links)

# 対象の文書リンクを配列の長さだけループ
for book_link in book_links:
    book_detail(book_link)
    break


# ページ中のH1タグがタイトル。これを元にファイルを生成
# divのid='text'配下に本文が格納されている
# 本文へのリンクは`title/X'となっている
# これの処理はあとで考える