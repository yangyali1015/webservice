#1.新手练习题
#1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def a(args):
#            if len(args)>5:#如果参数的长度大于5
#               print('这个对象的长度大于5')
#            elif len(args)==5:
#                print('这个对象的长度等于5')
#            else:
#               print('这个对象的长度小于5')


# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def a(list):
#     c=[]
#     if len(list)>2 :#如果参数的长度大于2
#         for b in list[0:2]:#遍历这个参数前两个值
#             c.append(b)#每次遍历加到c列表里面
#         return c  #最后返回c
#     else:
#            print('输入有误')
# haha=[1,2,3]
# print(a(haha))


# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。
# def name(a,b):
#     if type(a)==dict and type(b)==str:#判断参数类型
#         for c in a.values(): #遍历字典a
#          if b in c:         #判断字符串b 是否在字典的值中
#              return('{}在{}中'.format(b,a))  #如果在就返回这个数据
#          elif  b not in  c:    #如果不在
#              a['小芳']=b       #就把b赋值给小芳加入字典
#              print(a)
#              return a
# zidian={'小明':'17岁','小红':'16岁'}
# zifuchuan='18岁'
# print(name(zidian,zifuchuan))

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
# def a(age,jender,x,y,k):#定义一个函数为题目中的五个变量
#     sum_1 =0           #定义符合要求的人数初始值为0
#     count_1 =0       #定义采访的次数的人数初始值为0
#     while count_1<k:  #采访的次数要比K值小才开始循环
#       age=input('您的年龄是：') #年龄为询问的年龄
#       if int(age)>y or int(age) <x: #如果年龄不在范围内直接不满足要求，不需要问了
#         print('很抱歉您不符合我们的要求！')
#       elif x<=int(age)<=y:      #如果年龄满足要求再继续问性别
#         jender=input('请输入您的性别')
#         if jender =='m':       #如果性别也满足要求
#             print('恭喜你加入我们足球队！')
#             sum_1 += 1          #每次满足要求时符合要求的人数加1
#         else:
#             print('很抱歉您不符合我们的要求！')
#       count_1+=1               #不论符不符合，采访的次数都要加1
#       print('符合要求的人数为：{}'.format(sum_1))
# a('12','m',5,12,10)

 #进阶题
 # 1题
# a='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# #将字符串大写换小写，小写换大写。
# a.swapcase()
# print(a.swapcase())#输出结果为SDsDSFDaDSDSDFSFDSDasdsdfdsfA
# # #镜像字符串
# #  #ord()可以将字母转换为对应的十进制ASCII数值，大写的数值从中间平分，对应的和为155，小写的为219
# #  #所以只要知道前面的字母对应的十进制ASCII数值，就可以得出镜像的数值是多少
# #  #chr()函数将十进制ASCII数值转换为字母
# b=a.swapcase()  #将刚才转换的字符串赋值给b
# e=[]
# for c in b :    #遍历b里面的每一个字符串
#     if c.islower():  #如果是小写
#         c=chr(219-ord(c))#就按照小写字母对应的和减去这个小写字母对应的十进制ASCII数值
#         e.append(c)
#     elif c.isupper(): #如果是大写
#         c=chr(155-ord(c))#就按照大写字母对应的和减去这个小写字母对应的十进制ASCII数值
#         e.append(c)
# print(*e)#最后打印新的e

#第二种方法
a='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
tran=[]
#将字符串大写换小写，小写换大写。
for b in a:
    if b .islower():#如果是小写
        b=b.upper()#就将他转换为大写
        tran.append(b)#并且加入到空列表里面去
    elif b .isupper():
        b =b.lower()
        tran.append(b)
print(''.join(tran))
str=[]#将列表转换为字符串时用空字符取代逗号连接
for c in tran :    #遍历tran里面的每一个字符串
    if c.islower():  #如果是小写
        c=chr(219-ord(c))#就按照小写字母对应的和减去这个小写字母对应的十进制ASCII数值
        str.append(c)
    elif c.isupper(): #如果是大写
        c=chr(155-ord(c))#就按照大写字母对应的和减去这个小写字母对应的十进制ASCII数值
        str.append(c)
print(''.join(str))#最后打印新的字符串


#第二题
# import re
#
# string = "我的是名字是lemon,今年5岁。"
#
# #过滤字符串中的英文与符号，保留汉字
# str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", string)#匹配英文和符号转换为空格
#
# #\D 匹配一个非数字字符。等价于 [^0-9]
# num = re.sub("\D", "", string)
#
# #从字符串中提取字母字符串
# result = ''.join(re.findall(r'[A-Za-z]', string))#查找英文字母后用空格连接起来
#
# print("中文 : "+str)
# print("数字 : "+num)
# print("拼音 : "+result)
#
# p = re.compile(r'[-,。$()#+&*]')
# # 查找特定单个字符
# m = re.findall(p, string)
# s1 = ""
# for s in m:
#     s1 += s
#     # print(s1)
# print("符号 ： "+s1)
#
#
# #第二种方法
# string = "我的是名字是lemon,今年5岁."
# zimu=[]#定义一个空字母列表用于待会遍历出来的字母加到里面
# zifu=[]#定义一个空英文字符列表用于待会遍历出来的字母加到里面
# shuzi=[]#定义一个空数字列表用于待会遍历出来的字母加到里面
# hanzi=[]#定义一个空汉字列表用于待会遍历出来的字母加到里面
# for a in string:#遍历字符串
#     if 32<=ord(a)<=47 or 58<=ord(a)<=64 :#如果这个字符串的ASCII编码十进制数在这个范围内
#         # print('字符为:'+a)
#         zifu.append(a)                 #就把这个字符加到英文字符列表里
#     elif 91<=ord(a)<=96 or 123<=ord(a)<=126:
#         # print('e :'+a)
#         zifu.append(a)
#     elif 48<=ord(a)<=57 :
#         # print('数字为：'+a)
#         shuzi .append(a)
#     elif 65<=ord(a)<=90 or 97<=ord(a)<=122:
#         # print('字母为：' + a)
#         zimu.append(a)
#     else:                          #如果以上范围都不在那就是汉字
#         hanzi.append(a)
# print('字母为：',*zimu)           #打印列表顺便用* 号脱去中括号
# print('字符为：',*zifu)
# print('数字为：',*shuzi)
# print('汉字为：',*hanzi)
#




