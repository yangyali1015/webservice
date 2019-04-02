import requests
class Request():
    def __init__(self,url,param,method):
        self.url=url
        self.param=param
        self.method=method
    def http_request(self):
        if (self.method).upper()=='GET':
          resp=requests.get(self.url,params=self.param)
        elif (self.method).upper()=='POST':
          resp=requests.get(self.url,data=self.param)
        else:
            print('不支持该请求。')
            resp=None
        return (resp)
