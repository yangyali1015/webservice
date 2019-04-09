import os
file=os.path.realpath(__file__)
print(os.path.split(os.path.split(file)[0])[0])

excel_path=os.path.join(os.path.split(os.path.split(file)[0])[0],'data','web_excel.xlsx')
print(excel_path)

con_path=os.path.join(os.path.split(os.path.split(file)[0])[0],'conf','conf_web.conf')
print(con_path)

log_path=os.path.join(os.path.split(os.path.split(file)[0])[0],'result_log_report','py14_log')
print(log_path)

report_path=os.path.join(os.path.split(os.path.split(file)[0])[0],'result_log_report','py14.html')
