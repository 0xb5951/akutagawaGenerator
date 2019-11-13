# coding: UTF-8
import re
import requests
from bs4 import BeautifulSoup
import time

site_url = "https://aozorashoin.com"
auther_url = "https://aozorashoin.com/author/879"

#著者リストから書籍へのリンク一覧を抜き出す
def get_book_list(auther_url):
    r = requests.get(auther_url)
    soup = BeautifulSoup(r.text, "html.parser")
    author_page_a_tag = soup.find('table', class_="table-hover").find_all('a', href=re.compile('../title/.*'))

    book_links = [] 
    for a_tag in author_page_a_tag:
        book_links.append(str(a_tag.get('href').replace('..', '')))
    return book_links

# 文書ページからテキストのみを抜き出す
def book_detail(book_link):
    rb = requests.get(site_url + book_link)
    book = BeautifulSoup(rb.text, "html.parser")
    title = book.h1.text
    with open('./source/'+title+'.txt', mode='w') as f:
        f.write(str(book.select("#text")))
        print('installed' + title)
    time.sleep(5)
    return

if __name__ == "__main__":
    book_links = get_book_list(auther_url)
    for book_link in book_links:
        book_detail(book_link)