import os
path=os.path.realpath(__file__)
# print(path)

#excel表格路径
excel_path=os.path .join(os.path.split(path)[0],'excel_class.py')
print(excel_path)

#配置类路径
conf_path=os.path .join(os.path.split(path)[0],'conf_class.py')

#日志类路径
loger_path=os.path .join(os.path.split(path)[0],'loger_class.py')

#配置文件路径
conf=os.path .join(os.path.split(path)[0],'con_1.conf')

#请求类路径
http_path=os.path .join(os.path.split(path)[0],'http_class.conf')
#测试报告路径
report_path=os.path .join(os.path.split(path)[0],'py14班最胖的筱雪.html')