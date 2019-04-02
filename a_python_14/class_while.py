# #函数有啥作用:可以实现某个功能，重复使用
# # 提高代码的复用性
# f(x)=x+1
# type()
# len()
# range()
# #函数的语法：关键字def
# #函数的具体语法：
# def 函数名(参数1，参数2，参数3):
# #函数体：本函数要实现的功能
# #return表达式
# def 顶格写 表示这是一个函数
# 函数名 小写 不同的字幕与数字之间用下划线隔开
# 参数的个数可以大于等于0
# #函数体是函数的子代码 要有缩进
# #return后面的表达式可以大于等于0个
# return的作用就是当你调用函数的时候会返回return后面的表达式的值
# 如果return后面没有表达式，写没写没区别
# #如何调用函数 函数名（对应个数的参数
def radio():
     print('就是一个复读机')
     return [1,2,3]
     print(radio())

# def radio():
#     print('123')
#     return [1]
# print(radio())

print ('hello world')

# current_number=1
# while current_number<=6:
#     print(current_number)
#     current_number += 1
#     这条语句就是设置一个当前值为1，然后只要值小于等于6就继续循环
#     每循环一次就加1，一直到值大于6时才停止

#让用户选择何时退出
# a='请输入用户名'
# a+='\n请输出密码'
# message=''
# while message !='quit':
#     message=input(a)
#
#     if message!='quit':
#         print('输入有误请重新输入')

#使用标志，标志就是如果有很多条件，但必须都满足才能运行，就是满足的时候时True
#例如
# user ='早上好'
# user += '\n请输用户名和密码：'
# name = True
# while name:
#     message=input(user)
#     if message=='123':
#         name=False
#         print('正在进入。。。')
#     else:
#         print('请重新输入：')
#在这里name就是一个标志，也就是当name为真的时候才循环，
# 那什么时候为真呢，下面定义了当他等于quit 的时候时假的，其他时候时真的，
# 也就是只要你不输入quit那我就循环

#使用break退出循环,不需要定义一个标志，直接判断然后终止

# user ='早上好'
# user += '\n请输用户名和密码：'
# while True:
#     message=input(user)
#     if message=='123':
#         break
#     else:
#         print('请重新输入：')

# 可使用break 语句来退出遍历列表或字典的for 循环。
# 例如;
# a=['语文','数学','英语']
# for b in a :
#     print(b)
#     if b=='数学':
#       break
#     else:
#       print(666)

#在循环中使用continue 根据条件测试的结果决定是否继续执行循环，例如
# a=0
# while a<=10:
#     a+=1
#     if a%2==0: #如果a除以2等于0 ，那就说明是偶数就继续执行循环
#         continue
#     print(a)

#避免死循环
#使用while 循环来处理列表和字典
# a=['小明','小红','小芳']
# b=[]
# while a:
#     c=a.pop()
#     print(c)
# b.append(c)
# print(b)
# for d in b:
#     print(d)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
# confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# responses={}#创建一个新字典
# active =True
# while active:
#     name =input ('请问你的名字是什么')
#     response=input ('请问你喜欢爬山吗')
#     responses[name]=response#把名字和爱好写进字典
#     repeat=input('还有人要接受调查吗？')
#     if repeat=='no':
#         active=False
# for name,hobby in responses.items():#遍历字典
#     print('结果是'+name +response+'爬山')

dreams={}
active = True
while active:
    name = input ('您好，请问您怎么称呼？')
    dream = input ('请问你有什么梦想吗')
    dreams[name]=dream
    repeat = input('还要继续调查吗')
    if repeat == 'no':
        active =False
print('调查结果')
print(dreams)
for haha,value in dreams.items():
    print(name +'的梦想是：'+dream)