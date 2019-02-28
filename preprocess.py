# 取得した書籍の情報に対して前処理を行う。
# データには、書籍情報やルビ、注釈などが付随しているので、元の文のみを抜き出す。

import sys
import re

path = 'source/凶.txt'
file = open(path, 'r', encoding='Shift_JIS')

output = ""
# source_text = file.decode('Shift_JIS')

source_text = file.read()
# print(source_text)
# output = re.split(r'\r',source_text)
text = re.split(r'底本',source_text)
# text = text.replace('｜','')
text = re.sub(r'《.+?》','',text)
text = re.sub(r'［＃.+?］','',text)
# print(output)
print(text)

# file = open('test_preprocess.txt','a',encoding='utf-8').write(text)