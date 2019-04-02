#每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试 条件测试
#大小写不同也可能造成值不相等
# names=('xiaoxue','haha')
# for name in names:
#     if name!='xiaoxue':
#         print('你好')
# names=['xiaoming','xiaohong','xiaozhang']
# if 'xiaofang'in names:#可以使用in来判断你要的值在不在列表中
#     print('haha')
# #或者使用not in 来判断不在列表中
# if 'xiaofang'not in names:
#     print('oo')
#if else 如果if那里的是真的则输出if下面语句 ，如果是假的输出else下面语句
#if-elif-else 超过两个情形，例如
# age=18
# if age>20:
#     print('交20块钱')
# elif age ==20:
#     print('交30块钱')
# else :
#     print('免费')
#这种语句有一个毛病就是从上至下有一个通过了其他的就不会测试了
# 所以如果你想让程序把每一个都执行一遍就依次用if比如：
# names=['xiaohong','xiaozhang','xiaofang']
# if 'xiaofang' in names:
#     print(1)
# if 'xiaozhang' in names:
#     print(2)
# if 'xiaofang' in names:
#     print(3)
# #if可以先判断是不是为空在输出
# names=[]
# if names:
#     for name in names:
#         print('1')
# else:
#     print(2)
#
# a={'name':'huahua','pwd':'123456'}
# name=input('请输入用户名和密码')
# pwd=input('请输入密码')
# if  name=='huahua' and  'pwd'=='123456':
#     print('登陆成功')
# else:
#     print('请重新输入')

# 2.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，
# # 输出满足条件的总人数。
# person={'性别':['f','m'],'b':'age' }
# a=input('请输入性别 ')
# e=input('请输入年龄')
# for c ,d in person .items():
#     if 10<=d <=12:
#        if a ==c:
#          print('欢迎你加入')
#     else:
#         print('非常遗憾')
list1 = [[2, 3, 8, 4, 9, 5, 6], [5, 6, 10, 17, 11, 2]]
for a in list1:
    for b in a:
        print(b)






# a=input('性别')
# b=input('年龄')
# xingbie =['m','f']
# c=0
# while c <10:
#     if a==xingbie[1] and 10<=b<=12:
#         print('欢迎加入')
#     else:
#         print('很遗憾您不能加入')
#         c=c+1
#         break

