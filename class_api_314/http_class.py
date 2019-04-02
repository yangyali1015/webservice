import requests
class Request():
    def __init__(self,url,param,method,cookies):
        self.url=url#地址
        self.param=param#参数
        self.method=method#方法
        self.cookie=cookies#cookie
    def http_request(self):#发起请求
        if (self.method).upper()=='GET':
          resp=requests.get(self.url,params=self.param,cookies=self.cookie)#get请求
        elif (self.method).upper()=='POST':
          resp=requests.get(self.url,data=self.param,cookies=self.cookie)#post请求
        else:
            print('不支持该请求。')
            resp=None
        return (resp)

if __name__ == '__main__':

    global cookies
    cookies = {}
    URL= 'http://47.107.168.87:8080/futureloan/mvc/ap/loan/add'
    param={'mobilephone':13512365669,'pwd':'123456'}
    a=Request('http://47.107.168.87:8080/futureloan/mvc/api/member/login',param,'GET',cookies=cookies)
    print(a.http_request().text)
    resp=a.http_request()
    if resp.cookies !={}:
        cookies=resp.cookies
    b=Request('http://47.107.168.87:8080/futureloan/mvc/api/member/recharge',{'mobilephone':'11012345678','amount':'123456'},'GET',cookies=cookies)
    b.http_request()
    print(b.http_request().text)