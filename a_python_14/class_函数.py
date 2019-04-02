# def  a(b,c,d,e,f):
#      a=b+c+d+e+f
#      return a
# print(a(1,2,3,4,5))
# u=['zhanghhsan','admhhin','lihhsi','wanhhhgwu','duhhdu']

# a={'年龄':10,'身高':175}
# for b in sorted(a.keys):
#  print(b,end=' ')
# a=[1,3,5,2,8,4]
# b=[]
# while a:
#  e=min(a)          #排序
#  print(e)
#  a.remove(e)
#  b.append(e)
#  print(b)

# def a(b,c):
#  print(2)
#  return 1
# a(1,2)
# # e=a(1,2)
# # print(a(1,2))

# def display_message():
#      print('你好')
#      return 'hahah'
# a=display_message()
# if a=='hahah':
#  print('哎呀妈呀')

# def build_person(first_name, last_name, age=''):
#
#   person = {'first': first_name, 'last': last_name}
#   if age:
#    person['age'] = age
#   return person
# musician = build_person('jimi', 'hendrix', age=0)
# print(musician)

# def city_country(name,country):
#  c=(name+' 的国家是：'+country)
#  return c
# f=city_country('北京','中国')
# print(f)

# def make_album(name,zhuanji):
#  a = {'name_1': name, 'zhuanjiming': 'zhuanji'}
#  return a
# while True:
#  haha = input('请输入您的名字：')
#  if haha == 'q':
#   break
#  hehe = input('请输入您的专辑：')
#  if hehe == 'q':
#   break
#  b=make_album(haha, hehe)
#  print(b)
#
def name(names):
  for a in names:
    print('你好{}'.format(a))
  # return 'hahhahha'
b=['1','2','3','4']  #将列表写入函数
name(b)
# print(name(b))

# yaodayin=['haha','hehe','aiya']
# dayinhao=[]
# while yaodayin:
#  a=yaodayin.pop() #每次循环都删除最后一个元素
#  print('这个正在打印'+a)
#  dayinhao.append(a)#删除的元素就加到空列表说明这个正在打印
# for c in dayinhao:#遍历这个新列表，每次遍历说明这个元素打印好了
#    print('这个已经打印好了'+c)

#用函数的方法重复上面工作
# def dayinji(yaodayin,dayinhao):
#  while yaodayin:
#   a=yaodayin.pop()
#   print('这些正在打印'+a)
#   dayinhao.append(a)
#   # print(dayinhao)
# def name(dayinhao):
#   for b in dayinhao:
#     print('这些打印好了：'+b)
#
# c=['haha','aiya']
# d=[]
# dayinji(c,d)
# name(d)

# def show_magicians(name[:],lihai):
#  while name[:]:
#      b=name[:].pop()
#      lihai.append(b)
# def make_great(lihai ):
#  for c in lihai :                         #未解决的问题
#   print('the grate' +c)
#
# haha=['xiaoming','xiaohong','xiaozhang']
# hei=[]
# show_magicians(haha,hei)
# make_great(hei)

#
# def sanmingzhi(*tiaoliao):
#  print( '您点的三明治材料是：' )
#  for a in tiaoliao:
#   print(a)
#
# sanmingzhi('西瓜','黄瓜','西红柿')
# sanmingzhi('hahha','aiya','haoba')
#
# def users(name,height,**info):
#  a={}
#  a['names']=name
#  a['heights']=height
#  for key,value in info.items():
#   a[key]=value
#  return a
#
# haha=users('yangyali',175,爱好='kanshu')
# print(haha)

#定义函数
# def greet_user():
#     '''显示问候语'''
#     print('hello')
#这句话的def是告诉python这里要定义一个函数
#冒号后面的缩进叫做函数体
#三个引号文档字符串 （docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档
#代码行print("Hello!") （见❸）是函数体内的唯一一行代码，greet_user() 只做一项工作：打印Hello! 。
# def greet_1(username):#括号里的可以自己定义
#     '''这是问候语'''
#     print('你好啊'+username+'请输入密码')
# greet_1('王思聪')#调用函数的时候直接执行定义函数的代码

#实参和形参
#在函数greet_user() 的定义中，变量username 是一个形参 ——函数完成其工作所需的一项信息，括号里的东西不需要加引号
#在代码greet_1('王思聪')中，‘王思聪’是一个实参--实参是调用函数时传递给函数的信息

#传递实参
# 在传递实参的时候可以根据位置也就是索引向函数传递参数
# 你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参

# def pets(name,jender):
#     print('我有一只叫'+name+'的猫')
#     print('我的猫是'+jender+'的')
# pets('小花','女')
#函数可以多次调用，所以我们只需要定义好一个函数后可以不断调用
#位置实参的顺序很重要

#关键字实参
#关键字实参 是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆
# 例如
# 我们在调用函数的时候可以这样写 pets(name='小花'，jender='女')

#默认值，也就是在定义函数的时候括号里可以预先设定一些常用值，但是记得把没有设定的形参放在第一个，
# 因为你在调用的时候默认是从第一个开始赋值

#等效函数的调用
# 就是我可以利用位置给函数赋值，可以利用默认值，还可以利用关键字

#在调用函数时可以习惯性的加上一句 if __name__ == '__main__':
# 这样可以防止在其他模块调用函数的时候不需要的函数也打印出来

#range函数生成指定的整数序列，可迭代的数据类型
#range(m,n,k)m是开头，默认值为0，n结尾，k步长默认值为1   取左不取右，取头不取尾

# a=['yang','yali','maya','heng','e']
# a.extend(['haha','aiya'])#将列表添加到尾部，可以理解为列表与列表的拼接
# print(a)
# a.clear()#清空列表，返回一个空列表
# a.sort()#无返回值
# print(a)

#变量的作用域：全局变量，局部变量
#函数内的叫做局部变量，函数外叫全局变量
#有局部变量就用局部变量否则就用全局的
#如果在函数内部声明某个变量为全局变量用global.
msg='python14期'  #全局变量
def send_msg( ):
    global msg  #声明全局变量
    msg='哎呀'    #局部变量
    print('信息是{}'.format(msg))

print(msg)

#实际运用
#1，介绍requests--完成http请求
#常规用法：result=requests.get(url,data)--完成get请求
# result.url--得到你刚刚请求的url是什么
# result.text--得到响应的内容
# result.json--得到你的响应结果，并利用json直接转换为dict格式

