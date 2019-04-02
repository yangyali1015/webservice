import unittest
import HTMLTestRunnerNew
from class_api_314 import path_class
from class_api_314.cases_suit import TestCase
suite=unittest.TestSuite()#创建测试套件对象
loader=unittest.TestLoader()#创建对象
suite.addTest(loader.loadTestsFromTestCase(TestCase))#加载测试用例
with open(path_class.report_path,'wb') as file:
    runer=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)#测试报告
    runer.run(suite)#运行