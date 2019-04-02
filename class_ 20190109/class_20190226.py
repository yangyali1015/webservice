
#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串
from configparser import ConfigParser as cf
class conf_1:
    '''这是一个配置类'''
    def __init__(self,filename,section,option):
        self.filename=filename
        self.section=section
        self.option=option

    def getint(self):
        '''读取整数'''
        a = cf()#创建一个可以调用函数的对象
        a.read(self.filename,encoding='utf-8')#读取文件
        value=a.getint(self.section,self.option)#取值
        return value#返回值
    def getfloat(self):
        '''读取浮点数'''
        a = cf()
        a.read(self.filename,encoding='utf-8')#读取文件
        value=a.getfloat(self.section,self.option)
        return value
    def getboolean(self):
        '''读取布尔值'''
        a = cf()
        a.read(self.filename,encoding='utf-8')#读取文件
        value=a.getboolean(self.section,self.option)
        return value
    def getstr(self):
        '''读取字符串'''
        a = cf()
        b=a.read(self.filename, encoding='utf-8')#读取文件
        value =a.get(self.section, self.option)
        return value
    def get_other(self):
        '''读取其他类型'''
        a = cf()
        a.read(self.filename, encoding='utf-8')#读取文件
        value = a.get(self.section, self.option)
        value_1=eval(value)#转换到原始类型
        return value_1
if __name__ == '__main__':
    cf_1=conf_1('D:\\untitled\class_接口作业_312\con_1.conf','妈呀','button')
    # print(cf_1.getstr())
    # print(cf_1.getboolean())
    # print(cf_1.getfloat())
    # print(cf_1.getint())
    print(type((cf_1.get_other())))


