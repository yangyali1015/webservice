import unittest
from class_20190106.单元测试 import Math
#testcase类的一个实例就是一个测试用例
#testcase的初始化函数里面参数就是类里面方法名
class Test_math(unittest.TestCase):
   def test_add(self):
       Result = Math(3,4).add()
       expect = 3
       try:
         self.assertEqual(expect,Result)
       except Exception as e:
         print(Result)
# print(Math(3,4).add())

