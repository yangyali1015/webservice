# import pandas
# import openpyxl
# from openpyxl import workbook
# from openpyxl import load_workbook
# a=workbook.Workbook()
# a.save('maya.xlsx')
# wb=load_workbook('maya.xlsx')
# sheet=wb['Sheet']
# cell=sheet.cell(1,2,'hahhahh')
# a.save('maya.xlsx')
# a.close()
# pd=pandas.read_excel('maya.xlsx')
# print(pd.values)
import logging
from homework.logging_0227日志类.read_config import ReadConfig


class MyLog:

    def __init__(self):
        self.logger_name = ReadConfig('log.conf').get_str('LOG', 'logger_name')  # 收集器名字
        self.logger_level = ReadConfig('log.conf').get_str('LOG', 'logger_level')  # 收集器等级
        self.log_name = ReadConfig('log.conf').get_str('LOG', 'log_name')  # 日志文件名
        self.file_level = ReadConfig('log.conf').get_str('LOG', 'file_level')  # 日志文件等级
        self.stream_level = ReadConfig('log.conf').get_str('LOG', 'stream_level')  # 输出控制台渠道的等级
        self.formatter = ReadConfig('log.conf').get_str('LOG', 'formatter')  # 格式化

    def my_log(self, level, msg):
        """定义一个日志收集器并设置级别"""
        my_logger = logging.getLogger(self.logger_name)
        my_logger.setLevel(self.logger_level)

        # 指定输出渠道并设置级别及格式 StreamHandler--控制台
        ch = logging.StreamHandler()
        ch.setLevel(self.stream_level)  # 设置级别
        ch.setFormatter(self.formatter)  # 设置格式

        # FileHandler 输出指定文件并设置级别及格式
        fh = logging.FileHandler(self.log_name, encoding="utf-8")
        fh.setLevel(self.file_level)
        fh.setFormatter(self.formatter)

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
        my_logger.removeFilter(fh)
        my_logger.removeHandler(ch)

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


if __name__ == '__main__':
    log_test = MyLog()
    log_test.debug('哈哈哈哈哈哈哈哈哈哈')
