import unittest
from class_20190106 . class_单元测试练习 import *
import HTMLTestRunnerNew
suit=unittest.TestSuite()
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(Testcase))
# suit.addTest(Testcase('test_1'))
# suit.addTest(Testcase('test_2'))
# suit.addTest(Testcase('test_3'))
# loader=unittest.TestLoader()
# loader.loadTestsFromTestCase()
# loader.loadTestsFromModule()
with open('maya.html','wb') as file:
    runer=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='2019第一份报告',description=None,tester='筱雪')
    runer.run(suit)
