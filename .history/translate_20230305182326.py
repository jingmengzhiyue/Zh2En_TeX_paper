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

        


# if __name__ == '__main__':
#     Zh2En("你好，世界")