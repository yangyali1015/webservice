#异常：程序运行过程中出现的问题/错误都可以称之为异常
#每个异常包含的信息：出错的文件   行数   具体的代码   错误的类型  错误的信息——————可以定位完整的异常
#异常处理：当程序出现异常的时候，对异常进行处理
#try....except...
#try:
  #监控的代码块
#except:
  #如果监控的代码块出现问题，怎么处理
#遇到异常之前的代码会执行例如
try:
    file= open ('info.json','w',encoding='utf_8')
    file.read()
except:
    file.write('你好')#即使前面的语句出错了，但是他是在读的时候出错
                      #所以前面的打开语句还是可以执行，因此此处写不会报错
    print('读取错误')

#2 try...except... 错误类型  as  e....
#每个异常包含的信息：出错的文件   行数   具体的代码   错误的类型  错误的信息
#错误类型：Baseexception  exception  万能异常   缺点：逢错必抓  有内耗  优点：不会放过任何一个异常
#定位你的异常：明确你的错误类型  方便定位问题

#3课外查询python 标准异常。

#4注意：代码的执行顺序  什么地方会中断 跑到except里面去
       #一个异常里面可以写多个except
       #可以同时except多个异常
       #try里面可以嵌套try...except
#5 try...except...finally
    #不管你报不报错我都要执行这个finally下面的语句
    #什么时候用：
#6 debug调试 日志系统里面一个级别  最低的日志级别





# while True:#无限循环让用户输入内容
# a=input('请输入第一个数')
# # if a=='q':
# #     break
# b=input('请输入第二个数')
# # if b=='q':
# #     # break
# if a.isdigit()and b.isdigit():#判断用户输入的两个变量是数字
#     try:#尝试执行下面的代码块
#         answer=int(a)/int(b)
#     except:#如果发生错误就打印下面的语句
#         print('分母不能为0')
#     else:#如果没有发生错误就打印下面的结果
#         print(answer)
# else:#如果用户输入的不是数字就打印下面的语句
#     print('输入有误，分子或者分母应为数字')
# try:
#  with open('..\class_ 20190109\hahha','w+',encoding='utf-8') as file:
#         con_2=file.write('你好')
#         file.seek(0,0)
#         con_1 = file.read()
# except:
#         print('找不到文件')
# else:
#     print(con_1)
# def con_num(file):
#     '''定义一个数文本中有多少单词的函数'''
#     try:#尝试打开文件
#         with open (file,'r+',encoding='utf-8') as file_1:#打开文件
#             content=file_1.read()#定义阅读到的内容用变量content表示
#     except FileNotFoundError:#如果读取过程中发生错误就打印下面语句
#         pass#此处时让程序出现错误时直接过，不打印任何消息
#         # print('找不到{}文件，请查看文件是否在本目录中'.format(file))
#     else:#如果没有出现错误
#         # b=[]#定义一个空列表用来储存遍历文本时发现是小写字母就存到这个列表
#         con_num_1=content.split()#运用空格
#         # if 61<=ord(con_num_1)<=122:
#         #     b.append(con_num_1)
#         print(len(*con_num_1))
# a=['wenben2','wenben','hahha']#定义一个列表储存文本名称
# for file in a:#遍历这个列表里的每一个文本
#  con_num(file)#把每一个文本都调用上面的函数打开试试

#存储数据
#调用json模块
# import json
# name=1234
# file='name.json'
# with open (file,'w+') as file_1:
#     json.dump({'shenggao':176,'nianl':'12'},file_1)#dump的第一个参数时要进行存储为序列的变量，第二个参数时要存储到的文件名
#     file_1.seek(0,0)
    # print(type(file_1.read()))#123是字符串
    # json.load(file_1.read())
    # name_1=json.load(file_1)
    # for key in name_1:
    #  print(name_1[key])#把123转换为数字类型进行加减
# with open(file) as file_2:
#     name=json.load(file_2)
#     print(type(name))
# import json
# info=input('请输入用户名：')
# name='info.json'
# with open(name,'w+') as name_1:
#     json.dump(info,name_1)#dump函数没有返回值直接写入
#     print('我们会保存您的姓名')
# # with open(name) as name_1:
# #     name_2=json.load(name_1)#加载文件里的内容
# #     print('欢迎回来，{}'.format(name_2))
# import json
# def greet(name_1):
#     name_1='info3.json'
#     try:
#         with open(name_1) as name_2:
#             name_3=json.load(name_2)
#     except:
#         info3=input('请输入用户名：')
#         with open (name_1,'w') as name_4:
#             json.dump(info3,name_4)
#             print('我们将会存储您的姓名')
#     else:
#         print('欢迎回来！')
#
# greet('name_9')