import logging
class Logger():
    def __init__(self,filename='py14',fh_name='py14',loger_level='DEBUG',hander_level='DEBUG',msg_level='DEBUG',fomater='%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s'):
        self.filename=filename
        self.fh_name=fh_name
        self.loger_level=loger_level
        self.hander_level=hander_level
        self.msg_level=msg_level
        self.fomater=fomater

    def loger(self,msg):
        loger=logging.getLogger(self.filename)
        loger.setLevel(self.loger_level)

        fomater=logging.Formatter(self.fomater)
        ch=logging.StreamHandler()
        ch.setFormatter(fomater)
        fh=logging.FileHandler(self.fh_name,encoding='utf-8')
        fh.setFormatter(fomater)

        loger.addHandler(ch)
        loger.addHandler(fh)

        if (self.msg_level).upper()=='DEBUG':
            loger.debug(msg)
        elif (self.msg_level).upper()=='INFO':
            loger.info(msg)
        elif (self.msg_level).upper()=='WARNING':
            loger.warning(msg)
        elif (self.msg_level).upper()=='ERROR':
            loger.error(msg)
        elif (self.msg_level).upper()=='CRITICAL':
            loger.critical(msg)

        loger.removeHandler(fh)
        loger.removeHandler(ch)
    def debug(self,msg):
        Logger().loger(msg)
    def info(self,msg):
        Logger().loger(msg)
    def warning(self,msg):
        Logger().loger(msg)
    def error(self,msg):
        Logger().loger(msg)
    def critical(self,msg):
        Logger().loger(msg)

if __name__ == '__main__':
    Logger().error('maya')

