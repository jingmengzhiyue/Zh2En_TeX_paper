# Zh2En_TeX_paper

# 使用OpenAI以及YNMT创建论文

```mermaid
graph TB
    id1(开始)-->id2[访问YNMT/ChatGPT翻译模型]
    subgraph  
        id2==鉴权==>id3(向数据中心发送API与token)
        id3-->id4[鉴权通过]
        id3-->id5((结束))
        end
    subgraph 翻译
    	id4-->id6(按段落读取文章)
    	id6-->id7(送入翻译模型)
    	id7-->id8(获取返回值)
    	id8-->id9((创建TeX文档))
    	
    
    end
```
## 代码实现
main.py
```python 
from fnmatch import translate
from pylatex import Document, Section, Subsection, Command
from pylatex.base_classes import Environment
from docx import Document as docx_Document
from pylatex.utils import NoEscape
from pylatex.basic import NewLine
from translate import Zh2En
from pylatex.utils import italic, NoEscape
def fill_document(doc):
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))
        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')

class ABSTRACT(Environment):
    escape = False
    content_separator = "\n"
if __name__ == '__main__':
    doc = Document(default_filepath='paper',documentclass='IEEEtran',document_options='journal',lmodern=False,textcomp=False)
    doc.preamble.append(Command('title', 'Translate to English using the YNMT natural language translation model'))
    doc.preamble.append(Command('author', '***, ***'))
    doc.append(NoEscape(r'\maketitle'))
    with doc.create(ABSTRACT()):
        abstract = docx_Document(r"./abstract.docx")
        for p in abstract.paragraphs:
            abstrach_zh = p.text
            abstrach_en = Zh2En(abstrach_zh)
            doc.append(abstrach_en)
    with doc.create(Section('Introduction')):
        introduction = docx_Document(r"./introduction.docx")
        for p in introduction.paragraphs:
            introduction_zh = p.text
            introduction_en = Zh2En(introduction_zh)
            doc.append(introduction_en)
            doc.append(NoEscape(r'\par'))
    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()
```

调用YNMT函数获取翻译内容
translate.py

```python 
import sys
import uuid
import requests
import hashlib
import time
from imp import reload
import json
import time
import toml

reload(sys)
with open('authentication.toml', 'r') as f:
    token = toml.load(f)
    YOUDAO_URL = token['YOUDAO_URL']
    APP_KEY = token['YOUDAO_APP_KEY']
    APP_SECRET = token['YOUDAO_APP_SECRET']




def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def Zh2En(text):
    q = text

    data = {}
    data['from'] = 'zh-CHS'
    data['to'] = 'en'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = "2CBA59B4E493479FBBC1509DAD1C8F2D"

    response = do_request(data)
    contentType = response.headers['Content-Type']

        
    load_data = json.loads(response.content)
        
    out_text = load_data['translation']
    out = out_text[0]
    return out
```
