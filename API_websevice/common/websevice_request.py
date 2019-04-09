import suds
from suds.client import Client
from suds import sudsobject
from configparser import ConfigParser
from API_websevice.common.conf import Config
from API_websevice.common.class_re import read_re
from openpyxl import load_workbook
from API_websevice.common import path
import json
import re
from API_websevice.common.excel import Excel
class Request():
    def __init__(self,url,params):
        self.url=url#请求地址
        self.params=params#请求参数

    def web_request(self,method):#发起请求
        try:
            client = Client(self.url)#此处创建一个对象
            a= 'client.service.#method#(self.params)'#此处命名一个请求的字符串的原因时我要替换里面的方法名
            p = '#(.*?)#'  # 匹配格式
            m = re.search(p, a)  # 查找字符串里符合条件的字符串
            key = m.group(1)  # 去掉#号
            value =method  # 替换的值为模块名
            a = re.sub(p, value, a, count=1)
            result=eval(a)#发起请求
        except suds.WebFault as e:#获取参数出错的异常
            result =e.fault
            # print(ex.document)
        return json.dumps(sudsobject.asdict(result),ensure_ascii=False)#此处是将异常转换为字典格式再转换为字符串

if __name__ == '__main__':
    url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
    # client = Client(url)
    # params={'uid':'100006982','true_name':'筱雪雪','cre_id':429006199104089560}
    params ={'uid':'100006982','pay_pwd':'123','mobile':'#tel#','cre_id':'#IDCARD#','user_name':'USERNAME','cardid':'1234567897777','bank_type':'1001','bank_name':'中国银行'}
    result=Request(url,params).web_request('bindBankCard')
    print(result)
    # print(client)