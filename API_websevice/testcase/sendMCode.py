import unittest
import logging
import json
from suds import sudsobject
from ddt import ddt,data,unpack
from API_websevice.common import path
from API_websevice.common.conf import Config
from API_websevice.common.excel import Excel
from API_websevice.common.class_mysql import Mysql
from API_websevice.common.loger import Loger
from API_websevice.common.getdata import Getdata
from mysql import connector
from suds.client import Client
from API_websevice.common.websevice_request import Request
from API_websevice.common.loger import Loger

'''测试验证码接口'''

excel_object=Excel(path.excel_path,'sendMCode')
case_1=excel_object.read_excel()
# print(test_case)

@ddt
class TestsendMCode(unittest.TestCase):
    def setUp(self):
        print('====开始执行用例啦=====')
    def tearDown(self):
        print('====用例执行完毕====')
    @data(*case_1)
    def test_sendmcode(self,case):
         case_id=case['case_id']#用例id
         url=case['URL']#请求地址
         params=eval(case['Params'])#请求参数
         expect_result=case['ExcepectedResult']#期望结果
         method=case['Module']
         print('正在执行第{}条用例，参数是{}'.format(case_id,params))
         result=Request(url,params).web_request(method)#发起请求

         print('期望值是{}'.format(json.loads(json.dumps(eval(expect_result)))))
         print('实际结果是{}'.format(result))

         try:
             #一下断言转换几次原因是请求结果虽然已经再请求类里面转换成字典形式
             # 但是和python里的字典格式不一样缺少引号，所以我先转换成字符串再统一转换成字典进行比较
            self.assertEqual(json.loads(json.dumps(eval(expect_result),ensure_ascii=False)),json.loads(result))
            res='pass'
         except Exception as e:
            Loger().ERROR('断言出错啦，错误是{}'.format(e))
            res='fail'
            raise e
         finally:
             excel_object.write(case_id+1,9,str(result))
             excel_object.write(case_id + 1, 10, str(res))#写入结果



