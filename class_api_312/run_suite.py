import unittest
import HTMLTestRunnerNew
from class_api_312 import path_class
from class_api_312.cases_suit import TestCase
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCase))
with open(path_class.report_path,'wb') as file:
    runer=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
    runer.run(suite)