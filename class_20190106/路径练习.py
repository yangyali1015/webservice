# import os
# # real_path=os.path.realpath(__file__)
# # print(real_path)
# #
# # # 真实路径也就是绝对地址
# # real_path=os.path.realpath(__file__)
# # real_path=os.path.realpath(__file__)
# # pwd_path=os.getcwd()#获取当前工作目录
# # print(pwd_path)
# # file_list=os.listdir(pwd_path)
# # print(file_list)
# # print(os.listdir(os.getcwd()))
# # for a in file_list:
# #     if os.path.isdir(a):
# #         print()
# #         if os.path.isfile(a):
# #             print()
#
# # os.path.realpath(__file__)获取绝对地址
# # os.getcwd()获取当前目录
# # os.listdir(当前目录)获取当前目录下的所有文件夹
# # os.mkdir(文件名记得加引号)
# # os.rmdir(文件名记得加引号)
# import os
# realpath=os.path.realpath(__file__)
# file=os.getcwd()
# file_1=os.listdir(file)
# print(file_1)
a=[1,2,3]
d=[4,5]
f=[6,7,8]
for b in a :
    for c in d:
        for e in f:
            print(b,c,e)

