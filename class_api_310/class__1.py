from class_api_310 import class_excel
from class_api_310 import class_http
import unittest
from ddt import ddt,data,unpack



# print(type(case_1[0][0]))

@ddt
class Test_Register(unittest.TestCase):
  def setUp(self):
      print('------开始执行测试啦-------')
  def tearDown(self):
      print('------用例执行完毕啦------')
  case_1 = class_excel.Excel('case.xlsx', 'Sheet1').read()  # 读取EXCEl表格
  @data(*case_1)
  # @unpack
  def test_1(self,a):
      # print(a[0])
      if a[0] <= 5:#读取表格里面为注册的用例
              expect = a[5]  # 读取表格期望值
              url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
              params_1 = eval(a[4])  # 读取表格参数
              method_1 = a[3]  # 读取表格请求方法
              row = a[0] + 1
              # print(params_1)
              result= class_http.Http_1(url_1,params_1,method_1)#创建一个http请求对象
              result_1=result.method_1()#发起http请求
              # print(result_1)

              try:
                 self.assertEqual(expect,result_1)#判断期望值与实际结果
                 class_excel.Excel('case.xlsx', 'Sheet1').write(row, 8, 'pass')#如果出错就将pass写进表格
              except Exception as e:
                 print('断言错误{}'.format(e))
                 class_excel.Excel('case.xlsx', 'Sheet1').write(row, 8, 'failed')#如果出错就将failed写进表格
                 raise e
              finally:
                  ActualResult = class_excel.Excel('case.xlsx', 'Sheet1').write(row, 7, result_1)#最后无论报不报错都要将测试结果写进表格
      elif 6<=a[0]<=10:#读取表格里面为登录的用例
              expect = a[5]  # 读取表格期望值
              url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
              params_1 = eval(a[4])  # 读取表格参数
              method_1 = a[3]  # 读取表格请求方法
              row = a[0] + 1
              # print(params_1)
              result = class_http.Http_1(url_1, params_1, method_1)  # 创建一个http请求对象
              result_1 = result.method_1()  # 发起http请求

              try:
                  self.assertEqual(expect, result_1)
                  class_excel.Excel('case.xlsx', 'Sheet1').write(row, 8, 'pass')#如果出错就将failed写进表格
              except Exception as e:
                  print('断言错误{}'.format(e))
                  class_excel.Excel('case.xlsx', 'Sheet1').write(row, 8, 'failed')#如果出错就将failed写进表格
                  raise e
              finally:
                  ActualResult = class_excel.Excel('case.xlsx', 'Sheet1').write(row, 7, result_1)#最后无论报不报错都要将测试结果写进表格



