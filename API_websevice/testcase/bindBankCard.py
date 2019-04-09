import unittest
import logging
import json
import re
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

'''测试绑定银行卡接口'''

excel_object=Excel(path.excel_path,'bindBankCard')

case_1=excel_object.read_excel()
db=Config(path.con_path,'mysql','db_config').getother()#验证码的数据库
db_1={'host':'120.24.235.105','user':'python','password':'python666','port':3306,'database':'user_db'}#注册表的数据库
row_sql='select max(Fuid) from t_user_info '#用来查询注册表数据库行数的sql
# print(test_case)

@ddt
class TestbindBankCard(unittest.TestCase):
    def setUp(self):
        print('====开始执行用例啦=====')
    def tearDown(self):
        print('====用例执行完毕====')
    @data(*case_1)
    def test_sendmcode(self,case):
         case_id=case['case_id']#用例id
         url=case['URL']#请求地址
         params=eval(case['Params'])#请求参数
         expect_result=case['ExcepectedResult']#期望结果
         method=case['Module']#获取要测试的接口名称
         sql=case['Sql']#获取查询数据库的sql语句

         if case_id!=1:#如果这不是发送验证码的用例
             params= eval(read_re(case['Params']))#用正则匹配到参数里面的手机号和验证码用于注册
             #
             # print('第二个',getattr(Getdata, 'tel'))
             # print('第二个',getattr(Getdata, 'code'))
             # print('此处的参数是： ',params)
         print('正在执行第{}条用例，参数是{}'.format(case_id, params))
         before_max_row = Mysql(db_1, row_sql).select()[0]
         print('请求前的id', before_max_row)

         result=Request(url,params).web_request(method)#发起请求

         if case_id==1:#如果这是一条发送验证码的测试用例
             setattr(Getdata,'tel',str(params['mobile']))#那就将发送成功的手机号存到反射类
         after_max_row = Mysql(db_1, row_sql).select()[0]
         print('请求后的id',after_max_row,type(after_max_row))
         if case_id== 2:
             setattr(Getdata, 'uid', str(after_max_row))
             print('获取反射类里的uid是',getattr(Getdata,'uid'))
         print(getattr(Getdata,'tel'))

         if case['Sql']!=None:#如果表格里面的sql语句不为空
             # if case_id== 1:
                 case['Sql']=read_re(case['Sql'])#用正则匹配到验证码发送成功的手机号
                 sql=eval(case['Sql'])['sql']#匹配完成后将sql转换为字典取key
                 # print(sql)
                 msg_code=Mysql(db,(eval(case['Sql']))['sql']).select()[0]#从数据库查询到验证码
                 setattr(Getdata,'code',str(msg_code))#将验证码设置到反射类里
                 # print(msg_code)
         if  case_id== 3:
                 IDCARD=params['cre_id']
                 USERNAME=params['true_name']
                 setattr(Getdata, 'IDCARD', str(IDCARD))
                 setattr(Getdata, 'USERNAME', str(USERNAME))
         print('期望值是{}'.format(json.loads(json.dumps(eval(expect_result)))))
         print('实际结果是{}'.format(result))

         try:
             #以下断言转换几次原因是请求结果虽然已经在请求类里面转换成字典形式
             # 但是和python里的字典格式不一样缺少引号，所以我先转换成字符串再统一转换成字典进行比较
            self.assertEqual(json.loads(json.dumps(eval(expect_result),ensure_ascii=False)),json.loads(result))
            if case_id==2:#如果这是实名认证成功的用例
                a = eval(case['Params'])['user_id']  # 此处a是用户名

                sql = '''select Fmobile from t_user_info where Fuser_id=##'''  # 获取数据库手机号的sql
                sql = sql.replace('##', a)
                telephone = Mysql(db_1, sql).select()[0]  # 通过用户名查找数据库你的手机号格式
                after_max_row = Mysql(db_1, row_sql).select()[0]
                print('qingqiuhou d ',after_max_row,type(after_max_row))
                self.assertNotEqual(telephone, eval(case['Params'])['mobile'])  # 如果和表格里面的手机号不相等就是说明加密了
                self.assertEqual(before_max_row, after_max_row - 1)  # 判断注册成功后数据库是否增加一行数据（因为实名和注册是在同一个表）

            res='pass'
         except Exception as e:
            Loger().ERROR('断言出错啦，错误是{}'.format(e))
            res='fail'
            raise e
         finally:
             excel_object.write(case_id+1,9,str(result))
             excel_object.write(case_id + 1, 10, str(res))#写入结果



