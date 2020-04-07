import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    # print("random =",s)
    # print("ts= ",t)
    # print("salt= ",t+s)
    return t+s


def get_sign():
    return ' 6f8837aae52584ce632e1fb224b1f482'


def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
    #' 1584685303386'
        #'1585725759869'

form_data={
    'i':' 我和你都是中国人',
    'from':' AUTO',
    'to':' AUTO',
    'smartresult':' dict',
    'client':' fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv':' 0ed2e07b89acaa1301d499442c9fdf79',
    'doctype':' json',
    'version':' 2.1',
    'keyfrom':' fanyi.web',
    'action':' FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
