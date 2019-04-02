from configparser import ConfigParser
class Configer():
    def __init__(self,filename,section,option):
        self.filename=filename
        self.section=section
        self.option=option
        self.cf=ConfigParser()
    def getint(self):
        self.cf.read(self.filename,encoding='utf-8')
        value=self.cf.getint(self.section,self.option)
        return value
    def getfloat(self):
        '''读取浮点数'''
        self.cf.read(self.filename,encoding='utf-8')#读取文件
        value=self.cf.getfloat(self.section,self.option)
        return value
    def getboolean(self):
        '''读取布尔值'''
        self.cf.read(self.filename,encoding='utf-8')#读取文件
        value=self.cf.getboolean(self.section,self.option)
        return value
    def getstr(self):
        '''读取字符串'''
        self.cf.read(self.filename, encoding='utf-8')#读取文件
        value =self.cf.get(self.section, self.option)
        return value
    def get_other(self):
        '''读取其他类型'''
        self.cf.read(self.filename, encoding='utf-8')#读取文件
        value = self.cf.get(self.section, self.option)
        value_1=eval(value)#转换到原始类型
        return value_1

if __name__ == '__main__':
    cf=configer('D:\\untitled\class_接口作业_312\con_1.conf','妈呀','button')
    print(cf.get_other())
