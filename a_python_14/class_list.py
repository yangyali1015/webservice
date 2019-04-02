# 中括号括起来的数据都是列表，看类型type
# 空列表
t=[1]
# 列表里可以包含各种类型的数据，证书，浮点数。字符串，元祖
# 元素与元素之间用逗号隔开
# 取值方式：与字符串和元祖一样，根据索引值取值
# 嵌套取值怎么取
# 和元祖一样

# 增加
# 加在尾部；列表名.append(value)一次只能增加一个值
# 在指定的索引位置加元素;列表名.insert（i，value)一次只能增加一个值
# 添加列表  列表名.extend(第二个列表名)
a=[1,2,3]
t.extend(a)
print(t)
# 删除最后一个元素 列表名.pop()
# 删除指定索引位置的元素 列表名.pop(i)
#
# # t.reverse()函数：反向列表中元素，相当于把以前列表倒过来
# # t.sort()函数：对原列表进行排序 数字
# # 列表可以删除，元祖不能删除
#
# #在Python中，用方括号（[] ）来表示列表，并用逗号来分隔其中的元素。
# name=['xiaoming','xiaohong','xiaozhang','xiaohui']
# print(name)#输出的时候会连同中括号一起输出
# #如果要提取列表里面的数据，可以直接输出索引号， 例如：
# print(name[0])#直接写索引号的时候记得把中括号写进去,输出结果不带中括号
# print(name[0].title())#让小明的首字母大写
# #索引是从0开始数的，提取最后一个元素的时候索引为-1
# message='my brother have a name :'+name[0].title()+'.' #将列表里取出来的值组成一句话
# print(message)
# #修改列表：只需要将要修改的位置等于你要修改的内容，然后再输出原来的变量，例如
# a=['xiaoming','xiaohong','xiaozhang']
# a[0]='xiaozhang'
# print(a)#输出的是：['xiaozhang', 'xiaohong', 'xiaozhang']
# #如果我要添加一个内容到列表的末尾，则可以使用：变量名.append()例如：
# a.append('xiaohuihui')#直接在括号里写内容，不需要等于什么，然后输出
# print(a)
# #如果建一个空列表再添加，可以一个一个的在末尾使用append例如：
# names=[]
# names.append('xiaoming')
# print(names)
# names.append('xiaozhang')
# print(names)
# #在列表中插入元素 insert()，直接在括号里输入索引值，也就是你要添加的位置，然后逗号加内容
# names.insert(0,'xiaohua')
# print(names)
# #在列表中删除一个元素，使用del 变量名[索引值]   这种删除方法是终身删除，例如：
# del names[0]
# print(names)
# #使用pop()语句可以删除末尾元素然后使用这个值，就好像游戏里这个人被杀了，那这个被杀的位置就爆发一种效果
# new_name=names.pop()
# print(new_name)#输出的值就是你删除的内容，然后你还可以使用
# # pop() 括号内也可以写索引值直接删除提取出来
# # 可以直接选择一个值删除，当你不知道索引的时候，利用remove
# a=[1,2,3,4,5]
# a.remove(5)
# print(a)#那么5就被删除了
# a=[1,2,3,4,5]
# b=5
# a.remove(b)
# print(a)
# print('is'+str(b)+'haha')
# #使用sort对列表进行永久性排序，以字母排序
# a=['yali','huihui','jingjing','qunzi']
# a.sort()
# print(a)
# #使用相反的顺序进行排列，只需向sort() 方法传递参数reverse=True
# a.sort(reverse=True)#true必须大写否则会报错
# print(a)
# #sorted临时排序，比如
# a=['yali','huihui','jingjing','qunzi']
# print(sorted(a))#不需要重新定义a.sorted()这是错的
# print(a)#又变回以前的顺序了
# #倒着打印列表,不是按照字母顺序到这打印，而是从最后一个元素开始打印
# #reverse()永久性的修改元素排列顺序，但是可以恢复以前顺序，重新执行一遍reverse（）
# a.reverse()
# print(a)
# a.reverse()
# print(a)
# #获取列表的长度 len()
# print(len(a))
