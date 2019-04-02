print("Hello Python world!")
name='xiaoxue'
print(name)
print(name.title())
print(name.upper())
print(name.lower())
first_name='yang'
last_name='yali'
full_name=first_name+''+last_name
print(full_name)
print('hello!'+first_name.title()+last_name.upper()) #拼接符号+
print('python')
print('\tpython')# 前面加空格
print('python\n\tjava')#先换行再加空格，不可以先空格再换行
language='python   '
print(language)
print(language.rstrip())#rstrip()消除字符串末尾的空白,直接输出只能暂时的消除空白
#要想永久的消除空白就必须重新设置一个变量等于language.rstrip()例如：
a=language.rstrip()
print(a)
#lstrip()消除字符串开头空白
#strip()消除两端空白
print(language)
# 在python中如果字符串里面有单引号外面就用双引号
# 在Python中，可对整数执行加（+ ）减（- ）乘（* ）除（/ ）运算
print(2+3)
#Python使用两个乘号表示乘方运算：
print(2**3)
#Python还支持运算次序，因此你可在同一个表达式中使用多种运算。
# 你还可以使用括号来修改运算次序，让Python按你指定的次序执行运算
print((2+3)*3)
# 　使用函数str() 强制转换成字符串类型
age=23
print('happy'+str
(age)+'birthday')
