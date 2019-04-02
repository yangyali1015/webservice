# 1：编写一个日志类，能够实现输出文件到指定文件和console
import class_20190106
import logging
class Mylog:
    def __init__(self,filename,textname,level,msg,fomater_1='%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s',level_1='DEBUG',level_2='DEBUG'):
        self.filename=filename#日志收集器名称
        self.textname=textname#输出渠道为文件时的文件名
        self.level=level#信息的日志级别
        self.level_1=level_1#收集器日志级别
        self.level_2 = level_2#输出渠道日志级别
        self.msg=msg#日志信息
        self.format=logging.Formatter(fomater_1)
    def loger_1(self):#日志函数
        loger=logging.getLogger(self.filename)#设置日志收集器名字

        loger.setLevel(self.level_1)#设置日志收集器级别
        '''设置格式'''
        '''设置输出渠道为控制台'''
        ch=logging.StreamHandler()
        ch.setLevel(self.level_2)
        ch.setFormatter(self.format)

        '''设置输出渠道为文件'''
        dh=logging.FileHandler(self.textname,'a+',encoding='utf_8')
        dh.setLevel(self.level_2)
        dh.setFormatter(self.format)

        '''设置输出渠道和日志收集器对接'''
        loger.addHandler(ch)
        loger.addHandler(dh)
        '''判断日志信息级别'''
        if self.level=="DEBUG":
            loger.debug(self.msg)
        elif self.level=="INFO":
            loger.info(self.msg)
        elif self.level=="WARING":
            loger.warning(self.msg)
        elif self.level=="ERROR":
            loger.error(self.msg)
        elif self.level=="CRITICAL":
            loger.critical(self.msg)

        '''清除输出渠道'''
        loger.removeHandler(ch)
        loger.removeHandler(dh)
if __name__ == '__main__':

    myloger=Mylog('py14','text_1','DEBUG','出错啦同志们！')
    myloger.loger_1()

# 2：结合配置文件类实现日志类的可配置，具体参考老师的代码以及视频


# 3：结合日志类以及do_excel类，加上异常判断 与日志输出
