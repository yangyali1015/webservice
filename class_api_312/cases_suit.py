import unittest
from ddt import  ddt,data,unpack
import json
import openpyxl
from configparser import ConfigParser
from openpyxl import load_workbook
from class_api_312.conf_class import configer
from class_api_312 import  path_class
from class_api_312.excel_class import Doexcel
from class_api_312.loger_class import Logger
from class_api_312.http_class import Request

case = Doexcel('case.xlsx', 'Sheet1').read()

@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        Logger().info('.....开始执行条测试用例啦.....')
    def tearDown(self):
        Logger().info('.....用例执行完毕啦.....')

    @data(*case)
    def test_case(self,a):
        global TestResult
        # print(a)
        expect=a[6]
        url=a[2]
        method=a[4]
        param=eval(a[5])
        row = a[0] + 1
        b = Doexcel('case.xlsx', 'Sheet1')
        result_1=Request(url,param,method).http_request()

        Logger().info('正在执行的数据是{}，结果是{}'.format(param, result_1.json()))
        try:
            self.assertEqual(json.loads(expect),result_1.json())
            TestResult='pass'
        except Exception as e:
            Logger().error('断言出错啦，错误是{}'.format(e))
            TestResult = 'failed'
            raise e
        finally:
            b.write_back(row,9,TestResult)
            b.write_back(row,8,str(result_1.json()))
            # print(type(result_1))
