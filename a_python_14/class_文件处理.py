# with open()函数前面加with 可以让python确定什么时候关闭文件，不需要手动的写函数close（）
# file=open('hahha')
# content=file.read()
# print(file.read())
#这样读取后打印出来的文件后面会有一个空白行，因为光标读取到最后的时候是空白，要消除空白可以利用
# print(content.rstrip())
#如果文件和当前文件不在同一个目录，比如再当前文件夹的文件夹里
#可以直接打开例如
# with open('../class_ 20190109/hahha') as file_1:
#     #
#     # for a in range(5):
#     #     if a <=1:
#     # print(file_1.readlines())
#     b=file_1.readlines()
#     c=''
#     d = input('shuzi')
#     for a in b:
#        # print(a)
#        c+=a.rstrip()
#
#        if d in c:
#            print('在里面')
#
#     # print(c)
# with open('../class_ 20190109/hahha') as maya:
#     # print(maya.read())#直接读取时没有空行
#     # for a in maya:  #遍历打印的时候会有一个空行
#     #     print(a)
#     print(maya.readlines())
#替换字符串中的内容
# a='i like dogs'
# a.replace('dogs','cat')
# print(a.replace('ke','cat'))
# file=open ('../class_ 20190109/hahha','w+',encoding='utf-8')
# con=file.write('123我们a')
# file.seek(0,0)
# con_1=file.read()
# print(con_1)

file=open('../class_ 20190109/hahha','w+',encoding='utf-8')
a=1
while a<=5:
            b = input('经济鸭是傻子吗？')
            con=file.write( b)
            # con_1=file.write('')
            print('您好，{},'.format(b))
            a=a+1

