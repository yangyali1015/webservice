#for循环，列表名为复数,print语句都有缩进时同时执行，没有缩进的之执行一次
hahas=['xiaoming','xiaohong','xiaozhang']
for haha in hahas:   #冒号一定不能忘记for 语句末尾的冒号告诉Python，下一行是循环的第一行。
    print(haha)
    print(haha.title()+'你真棒'+'\n')
print('晚晴王八蛋')#这里没有缩进所以只显示一次
#使用for 循环处理数据是一种对数据集执行整体操作的不错的方式。
# 例如，你可能使用for 循环来初始化游戏——遍历角色列表，
# 将每个角色都显示到屏幕上；
# 再在循环后面添 加一个不缩进的代码块，在屏幕上绘制所有角色后显示一个Play Now按钮。
#创建数值列表
#函数range()可以生成一系列数字
for value in range(1,5):  #打印从一到5的数字，但是不会打印出5
    print(value)
#使用函数list()将range()结果直接转换为列表
numbers=list(range(1,6))
print(numbers)
#使用函数range() 时，还可指定步长。例如，下面的代码打印1~10内的偶数：
even_numbers=list(range(2,11,2))#这句话表示： 从2开始数，然后不断地加2，直到达到或超过终值（11）
print(even_numbers)
#打印1到10整数的平方列表
a=[]
for value in range(1,11):
    b=value**2
    a.append(b)
    print(a)
#还可以使用最大值，最小值等函数，例如
a=[1,2,3,4,5]
print(max(a))
#列表解析，就是用一行代码把刚才的代码总结出来
a=[value**2 for value in range(1,11)] # value**2就是你最后要显示的值，后面的for循环就是给value提供值
print(a)
#切片
a=['hah','bab','cc','dd','zz','maya']
print(a[0:5:2])
for a in a [0:2]:
    print(a.title()+'是最棒的')
#复制列表
