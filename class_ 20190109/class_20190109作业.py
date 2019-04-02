#第一题
# a =0
# b=1
# while b<=100:#当i小于等于100时循环
#   a+=b#每循环一次a加b
#   b+=1#每循环一次b 加1
# print (a)#打印a

#第二题
# a=0#定义一个变量初始值为0
# for b in range (10 ):#打印从1到10 的数字
#     a+=b
# print(a)#1到10求和

#第三题
# for a in range(5):
#     print("* " * (a+1))

#第四题
# for a in range(5):#循环5次
#     print("  " * (4 - a), end="")#打印空格数
#     print(" *  " * (a + 1))#打印星星数

#第五题
# print('九九乘法表')#定义一个名称
# for a in range (1,10):#定义一个变量从1到10循环9次
#      for b in range(a):#定义内循环第二个变量循环次数和a相同
#          b+=1          #每次循环一次b值加1
#          print('%d*%d=%-3d'%(b,a,a*b),end='')
#      print('')

#第六题利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：冒泡排序：小的排前面，大的排后面。
# a=[1,7,4,89,34,2]#定义一个列表
# for b in range(0,5) :#首先循环五次，以为6个数字只需要排五次
#     for c in range(0,len(a)-1):#然后再上一步循环一次后把剩下的再循环一次
#         if a[c]>a[c+1]:
#             a[c],a[c+1]=a[c+1],a[c]
#     b=b+1#每循环一次就少一次
# print(a)

#第七题有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
# a=[1,2,3,4]
# for b in range (1,5) :#循环从1到5
#     for c in range(1,5):#循环从1到5
#         for  d in range (1,5):#循环从1到5
#             if (b != c) and (b != d) and (c != d):
#                 print("%d%d%d" % (b, c, d))

#第八题求 0—7 所能组成的奇数个数
# a = 1   #首先定义一个个数
# c=0  # 初始值为0的总和，每循环一次加一个a
# for b in range(1,9):
#      if b ==1:
#         a = 4  #1位数的奇数个数为
#      elif b ==2:
#         a =4*7 #2位数的奇数个数为28
#      elif b>2:
#         a *=8   #当位数为3-8时，第一位的数字始终只有7个选择，最后一位的数字始终是4个（1.3.5.7），中间数字都有8个选择。
#      c +=a
#      print ('%d位数的奇数个数为%d'%(b,a))
# print ('总和为：sum=%d'%c)

#第九题
a=[('方便面',10),('薯片',7),('可乐',4)]#商品的名字/价钱
b=[]  #定义一个空列表装购买清单
employ = input('请输入您的工资')
active=1
if employ . isdigit():
 employ =int(employ)
 while True:
    for c in a:  # 遍历商品的key  和值
         e = input('请输入您要购买的商品')
         if e.isdigit():  #  如果输入的是数字
           e=int(e)
           if 0<e<=len(a):  # 判断这个数字是不是比商品长度小
             print(a[e])         #根据用户输入的数字打印商品清单的索引
             f=a[e]              #定义一个新变量f 用来存到购买清单
             if f[1]<employ:     #因为商品里面的元祖就两个元素，所以索引值为1 的就是价钱
                b.append(f)     #将商品添加到购买清单
                employ-=f[1]    #每循环一次工资就少对应商品价钱
                print("加入 %s 进购物车,余额是 %s"%(f,employ))
             else:               #如果工资比金额低
               print('您的余额不足')
           else:                 #如果用户输入的数字超过了长度
             print('商品不存在')
         elif e =='i':           #如果输入i就退出打印清单
           print('打印购物清单')
         for j in b:             #遍历清单列表
           print(j)             #打印购物清单
           print('您的余额是',employ)
           exit()
         else:
           print('请重新输入')