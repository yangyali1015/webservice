#unittest   pytest  是两个测试模块
#测试用例  序号 步骤 参数 期望结果
#执行用例  对比实际结果与期望结果
#生成测试报告

#unittest  里面的
#testcase类  专门写用例的
import unittest
from  class_20190106.class_单元测试练习 import MathMethod
class  TestMathod(unittest.TestCase):#继承
    #用例的写法：每一条用例就是一个方法  def  test_用例描述（self)
    #必须是test_开头否则不能识别
    #testcase里面的初始化函数methodname指的是每一条用例的方法名
    #用例执行的顺序和ASCII编码字母顺序有关
    def test_a_s_b(self):
        Resturt=MathMethod(5,6).a_b_s()
        expect=2
        try:
          self.assertEqual(Resturt,expect)
        except AssertionError as e:
          print('与期望值不符{}'.format(e))
        raise e
        print('绝对值是{}'.format(Resturt))

#首先导入unittest模块
然后一个测试类继承unittest.testcase
写测试用例之前写一个setup   teardown
然后写测试用例
然后将测试用例放到suit里面
suite=unittest.Testsuite()
suite.Addtestcase

