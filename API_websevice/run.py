import unittest
import logging
import json
import re
import HTMLTestRunnerNew
import sys
sys.path.append('./')
from API_websevice.common.class_re import read_re
from suds import sudsobject
from ddt import ddt,data,unpack
from API_websevice.common import path
from API_websevice.common.conf import Config
from API_websevice.common.excel import Excel
from API_websevice.common.class_mysql import Mysql
from API_websevice.common.loger import Loger
from API_websevice.common.getdata import Getdata
from mysql import connector
from suds.client import Client
from API_websevice.common.websevice_request import Request
from API_websevice.common.loger import Loger
from API_websevice.testcase import sendMCode
from API_websevice.testcase import verifiedUserAuth
from API_websevice.testcase import userRegister
from API_websevice.testcase import bindBankCard
suit=unittest.TestSuite()#创建测试套件的对象
loader=unittest.TestLoader()#创建加载用例的对象
suit.addTest(loader.loadTestsFromModule(sendMCode))
suit.addTest(loader.loadTestsFromModule(verifiedUserAuth))
suit.addTest(loader.loadTestsFromModule(userRegister))
suit.addTest(loader.loadTestsFromModule(bindBankCard))
with open(path.report_path,'wb') as file:
    runer=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='webservice_test',description='接口项目实战',tester='snow')
    runer.run(suit)#执行用例
