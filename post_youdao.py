import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

form_data={
    'i':' 我和你都是中国人',
    'from':' AUTO',
    'to':' AUTO',
    'smartresult':' dict',
    'client':' fanyideskweb',
    'salt':' 15846853033868',
    'sign':' 6f8837aae52584ce632e1fb224b1f482',
    'ts':' 1584685303386',
    'bv':' 0ed2e07b89acaa1301d499442c9fdf79',
    'doctype':' json',
    'version':' 2.1',
    'keyfrom':' fanyi.web',
    'action':' FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
