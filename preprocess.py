# 取得した書籍の情報に対して前処理を行う。
# データには、書籍情報やルビ、注釈などが付随しているので、元の文のみを抜き出す。

import sys
import re
import os

path = './source/藪の中.txt'
file = open(path, 'r', encoding='Shift_JIS')

source_text = file.read()

count = source_text.count('\n')
print(count)

text_tagging_hi = re.sub(r'--+', 'タグを埋め込みます', source_text)
text_remove_tag = text_tagging_hi.split('タグを埋め込みます')[-1]
text_without_rubi = re.sub(r'《.+?》','', text_remove_tag)
text_without_com = re.sub(r'［.+?］', '', text_without_rubi)
output = text_without_com.split('底本')[0]
print(output)

file = open('test_preprocess.txt','a',encoding='utf-8').write(output)
