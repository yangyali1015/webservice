import requests
import json
url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'
params={'mobilephone':'13129980530','pwd':'123456','regname':'自闭患者'}
resp=requests.get(url,params=params)
# print(resp.text)
a=resp.text
print(type(json.loads(a)))
