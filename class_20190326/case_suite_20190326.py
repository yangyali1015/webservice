import sys
sys.path.append('./')
print(sys.path)

import unittest
import HTMLTestRunnerNew
import logging
from configparser import ConfigParser
from class_20190326.conf_20190326 import Config
from class_20190326.excel_20190326 import DoExcel
from class_20190326 import case_register_20190326
from class_20190326 import case_add_20190326
from class_20190326 import case_bidLoan_20190326
from class_20190326 import case_login_20190326
from class_20190326 import case_recharge_20190326
from class_20190326 import case_register_20190326
from class_20190326 import case_withdraw_20190326
from class_20190326 import class_re
from class_20190326 import case_path
from class_20190326 import conf_20190326
from class_20190326.loger_20190326 import Loger

# #
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(case_register_20190326))
suite.addTest(loader.loadTestsFromModule(case_login_20190326))
suite.addTest(loader.loadTestsFromModule(case_recharge_20190326))
suite.addTest(loader.loadTestsFromModule(case_withdraw_20190326))
suite.addTest(loader.loadTestsFromModule(case_add_20190326))
suite.addTest(loader.loadTestsFromModule(case_bidLoan_20190326))
with open('py14.html','wb')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试',description='这是一系列的测试报告',tester='筱雪')
    runner.run(suite)
# format=Config('D:\\untitled\class_20190326\con_20190326','log','format').getstr()
# Loger().DEBUG('测试日志')