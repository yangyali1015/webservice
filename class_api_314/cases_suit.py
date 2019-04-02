import unittest
from ddt import  ddt,data,unpack
import json
import openpyxl
from configparser import ConfigParser
from openpyxl import load_workbook
from class_api_314.conf_class import configer
from class_api_314 import  path_class
from class_api_314.excel_class import Doexcel
from class_api_314.loger_class import Logger
from class_api_314.http_class import Request

cases = Doexcel('case_2.xlsx','Sheet1','Sheet2').read()
# print(case)
cookies = {}
@ddt
class TestCase(unittest.TestCase):

    def setUp(self):
        Logger().info('.....开始执行条测试用例啦.....')
    def tearDown(self):
        Logger().info('.....用例执行完毕啦.....')


    @data(*cases)
    def test_case(self,a):
        global cookies

        # print(a)
        case_id=a['case_id']
        expect=a['ExcepectedResult']#期望值
        url=a['URL']
        method=a['Method']
        param=eval(a['Params'])
        # row = a[0] + 1
        b = Doexcel('case_2.xlsx', 'Sheet1','Sheet2')#创建表格类对象
        result_1=Request(url,param,method,cookies=cookies).http_request()#响应结果
        if result_1.cookies!={}:#如果响应的cookie 不为空
            cookies=result_1.cookies#重新赋值给全局变量cookies
        # print(type(result_1.json()))
        Logger().info('正在执行的第{}条用例，数据是{}，结果是{}'.format(case_id,param, result_1.json()))
        try:
            self.assertEqual(eval(expect), result_1.json())#断言
            TestResult = 'pass'
        except Exception as e:
            Logger().error('断言出错啦，错误是{}'.format(e))
            TestResult = 'failed'
            raise e
        finally:
            b.write_back(a['case_id'] + 1, 9, TestResult)#写入测试结果
            b.write_back(a['case_id'] + 1, 8, result_1.text)#写入实际
