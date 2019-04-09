from mysql import connector
from API_websevice.common.conf import Config
from API_websevice.common import path
from configparser import  ConfigParser

class Mysql():
    def __init__(self,db,sql,flag=1):
        self.db=db
        self.sql=sql
        self.flag=flag#等于1就默认返回一条数据
    def select(self):
        cnn=connector.connect(**self.db)#链接数据库
        cursor=cnn.cursor()#获取游标
        cursor.execute(self.sql)#执行sql
        if self.flag==1:
            res=cursor.fetchone()#返回一条
        else:
            res = cursor.fetchall()#返回全部
        return res

if __name__ == '__main__':
    db=Config(path.con_path,'mysql','db_config').getother()
    sql='select Fverify_code from t_mvcode_info_6 where Fmobile_no=13412345678'
    res=Mysql(db,sql).select()
    print(type(res[0]))