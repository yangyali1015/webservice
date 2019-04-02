import requests
class Http_1():
    def __init__(self,url,param,method):
        '''url :接口地址
           params:参数
           method:请求方法'''
        self.url=url
        self.param=param
        self.method=method
    def method_1(self):
        if self.method=='GET':
            res=requests.get(self.url,params=self.param)#get请求方法
            return (res.text)#返回响应数据
        elif self.method=='POST':
            res= requests.post(self.url, data=self.param)#post请求方法
            return (res.text)
if __name__ == '__main__':
    a=Http_1('http://47.107.168.87:8080/futureloan/mvc/api/member/register',
             {'mobilephone': '13121893530', 'pwd': '123456','regname':'小小雪'}
             ,'GET')
    print(a.method_1())
    # if a.method_1()=={"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}:
    #     print('ok')
    # else:
    #     print('失败')