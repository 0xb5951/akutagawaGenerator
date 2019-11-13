# coding:utf-8
# 取得した書籍の情報に対して前処理を行う。
# データには、書籍情報やルビ、注釈などが付随しているので、元の文のみを抜き出す。

import sys
import re
import os

source_path = './source/'

def preprocess():
    book_sources = os.listdir(source_path)

    for book_txt in book_sources:
        book_source = source_path + book_txt
        print('now processing:\t' + book_txt)
        with open(book_source, 'r', encoding='utf-8') as f:
            source_text = f.read()
            # htmlタグを削除
            output = re.sub(r'<.+?>','', source_text)
            # ふりがなを削除
            output = re.sub(r'（.+?）','', output)
            # 注釈を削除
            output = re.sub(r'［.+?］','', output)
            # その他邪魔オブジェクトを削除
            output = re.sub(r'[\[）\]]*','', output)
            file = open('preprocess_done.txt','a',encoding='utf-8')
            file.write(output)
            file.close()
    return             

if __name__ == '__main__':
    print('preprocess start')
    preprocess()

