from class_api_310 import class__1
import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()#添加测试套件
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(class__1.Test_Register))#以类的方式添加用例
with open('report.html','wb') as file:
    runer=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='2019第一份报告',description=None,tester='筱雪')
    runer.run(suite)#执行用例