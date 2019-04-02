# 第一题第一种解法
# a=float(input('学生分数为：'))
# if 0<=a<=100:
#     if 90 <= a <=100 :
#       print('优秀')
#     elif 60<=a<90:
#       print('合格')
#     else:
#       print('不及格')
#第一题第二种解法
# a=float(input('学生分数为：'))
# if 90 <= a <=100 :
#       print('优秀')
# elif 60<=a<90:
#       print('合格')
# elif 0<=a<60:
#       print('不及格')
# else:
#     print('您的输入有误，请重新输入')

#第二题第一种解法
# price =float(input('请问您的购买价格是多少'))
# if price>=0:
#  if 50 <= price <=100:
#      print('我们将会给您10%折扣，您的最终价格是：' , (price*(1-0.1)))
#  elif price >100:
#      print('我们将会给您20%折扣，您的最终价格是：',(price*(1-0.2)))
#  else:
#      print('对不起您的消费金额不能享受折扣 !' )
#第二题第二种解法
# price =float(input('请问您的购买价格是多少'))
# if 0<=price<50:
#     print('对不起您的消费金额不能享受折扣 !')
# elif 50 <= price <=100:
#      print('我们将会给您10%折扣，您的最终价格是：' + str((price*(1-0.1))))
# elif price >100:
#      print('我们将会给您20%折扣，您的最终价格是：'+str((price*(1-0.2))))
# else:
#     print('价格输入有误')

#第三题第一种解法
# n=int(input('请输入一个数字'))
# if n%15==0:
#     print('该数字可以被3和5同时整除。')
# else:
#     print('该数字不能同时被3和5整除。')
#第三题第二种解法
# n=int(input('请输入一个数字'))
# if n%3==0 and n%5==0:
#     print('该数字可以被3和5同时整除。')
# else:
#     print('该数字不能同时被3和5整除。')

#第四题第一种解法
# year=int((input('请输入一个年份')))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('这个年份是闰年')
# else:
#     print('这个年份不是闰年')
# #第四题第二种解法
# year=int((input('请输入一个年份')))
# if year%4==0 and year%100!=0 :
#      print('这个年份是闰年')
# elif year%400==0:
#      print('这个年份是闰年')
# else:
#     print('这个年份不是闰年')

#第五题 第一种解法
# a=input('请输入一个五位数：')
# if a[4]==a[0] and a[3]==a[1]:
#     print('这是一个回文数')
# else:
#     print('这不是一个回文数')
#第五题第二种解法
# c=[]
# a=input('请输入一个五位数：')
# for b in a :
#     c.append(a)
# if c[4]==c[0] and c[3]==c[1]:
#     print('这是一个回文数')
# else:
#     print('这不是一个回文数')

#第六题第一种解法
# a=input('请输入一个数字')
# import random
# b=random.randint(1,10)
# print('随机数字是:'+b)
# if int(a)>b :
#       print('bigger')
# elif int(a)==b:
#       print('equal')
# else:
#       print('less')
#第六题第二种解法
# a=int(input('请输入一个数字'))
# import random
# b=random.randint(1,10)
# print('随机数字是:', b)
# if  a!=b :
#     if a >b:
#       print('bigger')
#     elif a<b:
#       print('less')
# else:
#       print('equal')

# #第七题
# pingjia_orders ={'手撕包菜':'10元','香干肉丝':'10元','土豆丝':'10元','胡萝卜炒肉':'10元'}
# liangcai_orders ={'凉拌黄瓜':'10元','凉拌皮蛋':'10元'}
# xiaoguoxianchao_orders= {'大盆花菜':'16元','红烧鱼块':'18元'}
# print('我们有如下几样菜：’pingjia_orders‘,’liangcai_orders‘,’xiaoguoxianchao_orders')
# c=['pingjia_orders','liangcai_orders','xiaoguoxianchao_orders']
# order= input('您好请问您想吃点什么？')
# d=[]
# if order == c[0]:
#      print('您好有如下菜:')
#      print(pingjia_orders)
#      for cai_oder  in pingjia_orders :
#          d.append(cai_oder)
#      e=input('请选择菜名')
#      if e in d:
#             print('您好:'+e + pingjia_orders[cai_oder])
#      elif e not in d :
#            print('对不起，您要的菜这里没有')
# elif order == c[1]:
#     print('您好有如下菜:')
#     print(liangcai_orders)
#     for cai_oder in liangcai_orders:
#         d.append(cai_oder)
#     e = input('请选择菜名')
#     if e in d:
#         print('您好:'+e + liangcai_orders[cai_oder])
#     elif e not in d:
#         print('对不起，您要的菜这里没有')
# elif order == c[2]:
#     print('您好有如下菜:')
#     print(xiaoguoxianchao_orders)
#     for cai_oder in xiaoguoxianchao_orders:
#         d.append(cai_oder)
#     e = input('请选择菜名')
#     if e in d:
#         print('您好:'+e + xiaoguoxianchao_orders[cai_oder])
#     elif e not in d:
#         print('对不起，您要的菜这里没有')
#
#
#
#第二种解法
pingjia_orders ={'手撕包菜':'10元','香干肉丝':'10元','土豆丝':'10元','胡萝卜炒肉':'10元'}
liangcai_orders ={'凉拌黄瓜':'10元','凉拌皮蛋':'10元'}
xiaoguoxianchao_orders= {'大盆花菜':'16元','红烧鱼块':'18元'}
print('我们有如下几样菜：’pingjia_orders‘,’liangcai_orders‘,’xiaoguoxianchao_orders')
print('每种菜的菜单如下：')
a={'pingjia_orders':{'手撕包菜':'10元','香干肉丝':'10元','土豆丝':'10元','胡萝卜炒肉':'10元'},'liangcai_orders':{'凉拌黄瓜':'10元','凉拌皮蛋':'10元'},'xiaoguoxianchao_orders':{'大盆花菜':'16元','红烧鱼块':'18元'}}
for b,c in a .items():
    print(b,c)
oder=input('请问您需要点什么菜？')
if oder in a.keys():
 new_order=input('请问您的菜名是什么')
 for e in a[oder].keys():
    if new_order==e:
        print('您好:'+new_order + (a[oder][e]))
elif new_order !=e:
        print('我们这里没有这种菜')





