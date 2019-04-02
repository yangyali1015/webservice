# 0227-Python logging日志类
# 1：编写一个日志类，能够实现输出文件到指定文件和console
# 3：结合日志类以及do_excel类，加上异常判断 与日志输出
import logging

# 日志收集器logger 默认日志收集器root logger
# class MyLog:
#     def my_log(self):
#         """定义一个日志收集器并设置级别"""
#         my_logger = logging.getLogger("python27")
#         my_logger.setLevel("INFO")
#
#         # 指定输出渠道并设置级别及格式 StreamHandler--控制台
#         formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息:%(message)s]')
#         ch = logging.StreamHandler()
#         ch.setLevel("WARNING")  # 设置级别
#         ch.setFormatter(formatter)  # 设置格式
#
#         # FileHandler 输出指定文件并设置级别及格式
#         fh = logging.FileHandler("test.log", encoding="utf-8")
#         fh.setLevel("ERROR")
#         fh.setFormatter(formatter)
#
#         # 对接 输出两者的交集
#         my_logger.addHandler(ch)  # 输出到控制台
#         my_logger.addHandler(fh)  # 输出到指定文件
#
#         my_logger.debug("debug msg")
#         my_logger.info("今天天气真好！")
#         my_logger.warning("this is warning msg")
#         my_logger.error("报错了")
#         my_logger.critical("critical msg")
#
#         # 避免日志中出现重复信息，一定要记得移除
#         my_logger.removeFilter(fh)
#         my_logger.removeHandler(ch)
#
#
# if __name__ == '__main__':
#     MyLog().my_log()

# 2：结合配置文件类实现日志类的可配置
from class_20190106.read_config import ReadConfig
# res=ReadConfig('log.conf').get_str('LOG', 'logger_level')
# print(res)

#
class MyLog():
#
    def __init__(self):
        self.logger_name = ReadConfig('log.conf').get_str('LOG', 'logger_name')  # 收集器名字
        self.logger_level = ReadConfig('log.conf').get_str('LOG', 'logger_level')  # 收集器等级
        self.log_name = ReadConfig('log.conf').get_str('LOG', 'log_name')  # 日志文件名
        self.file_level = ReadConfig('log.conf').get_str('LOG', 'file_level')  # 日志文件等级
        self.stream_level = ReadConfig('log.conf').get_str('LOG', 'stream_level')  # 输出控制台渠道的等级
        self.formatter =logging.Formatter( ReadConfig('log.conf').get_str('LOG', 'formatter'))  # 格式化

    def my_log(self, level, msg):
        """定义一个日志收集器并设置级别"""
        my_logger = logging.getLogger(self.logger_name)
        my_logger.setLevel(self.logger_level)

        # 指定输出渠道并设置级别及格式 StreamHandler--控制台
        format=logging.Formatter(self.formatter)
        ch = logging.StreamHandler()
        ch.setLevel(self.stream_level)  # 设置级别
        ch.setFormatter(format)  # 设置格式

        # FileHandler 输出指定文件并设置级别及格式
        fh = logging.FileHandler(self.log_name, encoding="utf-8")
        fh.setLevel(self.file_level)
        fh.setFormatter(format)

        # 对接 输出两者的交集
        my_logger.addHandler(ch)  # 输出到控制台
        my_logger.addHandler(fh)  # 输出到指定文件

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 避免日志中出现重复信息，一定要记得移除


    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)

    # my_logger.removeFilter(fh)
    # my_logger.removeHandler(ch)

if __name__ == '__main__':
    res=MyLog()
    res.info('hah')
