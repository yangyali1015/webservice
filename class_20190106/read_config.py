# 写一个配置类 有以下几个函数：
# 1：读取整数
# 2：读取浮点数
# 3：读取布尔值
# 4：读取其他类型的数据 list tuple dict eval（）
# 5：读取字符串

from configparser import ConfigParser


class ReadConfig:  # 一个配置类
    def __init__(self, file_name):
        self.cf = ConfigParser()  # 创建对象
        self.cf.read(file_name, encoding='utf-8')  # 打开文件

    def get_str(self, section, option):
        # 读取字符串
        value = self.cf.get(section, option)  # 读取内容
        return value

    def get_int(self, section, option):
        # 读取整数
        value = self.cf.getint(section, option)  # 读取内容
        return value

    def get_float(self, section, option):
        # 读取浮点数
        value = self.cf.getfloat(section, option)  # 读取内容
        return value

    def get_boolean(self, section, option):
        # 读取布尔值
        value = self.cf.getboolean(section, option)  # 读取内容
        return value

    def get_other_data(self, section, option):
        # 读取元组 字典 列表等类型的数据
        value = self.cf.get(section, option)  # 读取内容
        return eval(value)  # eval()函数  转换为原来的数据类型


if __name__ == '__main__':
    res = ReadConfig('log.conf').get_str('LOG', 'logger_name')
    print(res)
