import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return ' 15846853033868'


def get_sign():
    return ' 6f8837aae52584ce632e1fb224b1f482'


def git_ts():
    import time
    t=time.time()
    ts=str(int(round(t*1000)))
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
    'ts': git_ts(),
    'bv':' 0ed2e07b89acaa1301d499442c9fdf79',
    'doctype':' json',
    'version':' 2.1',
    'keyfrom':' fanyi.web',
    'action':' FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
