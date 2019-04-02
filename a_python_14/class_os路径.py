import os
real_path=os.path.realpath(__file__)
print('绝对路径是：',real_path)

pwd_path=os.getcwd()#具体到当前工作目录
print('当前工作目录：',pwd_path)

file_list=os.listdir(pwd_path)#返回值是列表
print(file_list)#当前目录的所有文件

for a in file_list:
    if os.path.isdir(a):
        print('{}是文件夹'.format(a))
    elif os.path.isfile(a):
        print('{}是文件'.format(a))
#
# #新建删除文件夹
# os.mkdir('哈哈')  #新建在当前目录下也就是python4下面
# # os.rmdir('哈哈')#移除文件夹
# os.mkdir('哈哈/哎呀')#多级新建，要首先创建好哈哈然后再添加子文件夹
# os.rmdir('哈哈/哎呀')#删除的是哎呀这个文件不会删除哈哈这个文件夹
# os.rmdir('哈哈')#如果哈哈里面有文件不能直接删除，必须确认文件夹里没有文件才可以删除
#
# os.path.join(pwd_path,'那年夏天')
# os.mkdir(os.path.join(pwd_path,'那年夏天'))#在自目录下新建一个那年夏天
# os.path.join(pwd_path+'\那年夏天')