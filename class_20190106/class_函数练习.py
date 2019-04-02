# def display_message(study):
#     '''在本章学习到的东西'''
#     print('在本章我学到了'+study)
# display_message('python')
#
# def favorite_book(name):
#     '''最喜欢的书名'''
#     print('我最喜欢的书是'+name)
# favorite_book('英语')
#
# def make_shirt(size='L',ziyang='I love Python'):
#     '''尺码和字样'''
#     print('这是一件尺码为：'+ size+'的'+ziyang)
# # make_shirt(20,'牛逼')
# # make_shirt(size=20,ziyang='牛逼')
# make_shirt()

# def name(a,b):
#     sum=a+b
#     return sum
# c=name(2,4)
# haha=c+5
# print(haha)
#
# def name(**args):
#     return args
# name(a=123,b=456)
# c=name(a=123,b=456)
# for i in c:
#     print(i)
# if __name__ == '__main__':
#  a='hello python14'
#  b={'name':'123','haha':'456'}
#  for key,value in b .items():
#     print(a.join(key))
#     print(a.join(value))

string = "我的是名字是lemon,今年5岁."
zimu=[]#定义一个空字母列表用于待会遍历出来的字母加到里面
zifu=[]#定义一个空英文字符列表用于待会遍历出来的字母加到里面
shuzi=[]#定义一个空数字列表用于待会遍历出来的字母加到里面
hanzi=[]#定义一个空汉字列表用于待会遍历出来的字母加到里面
for a in string:#遍历字符串
    if 32<=ord(a)<=47 or 58<=ord(a)<=64 :#如果这个字符串的ASCII编码十进制数在这个范围内
        # print('字符为:'+a)
        zifu.append(a)                 #就把这个字符加到英文字符列表里
    elif 91<=ord(a)<=96 or 123<=ord(a)<=126:
        # print('e :'+a)
        zifu.append(a)
    elif 48<=ord(a)<=57 :
        # print('数字为：'+a)
        shuzi .append(a)
    elif 65<=ord(a)<=90 or 97<=ord(a)<=122:
        # print('字母为：' + a)
        zimu.append(a)
    else:                          #如果以上范围都不在那就是汉字
        hanzi.append(a)
print('字母为：',*zimu)           #打印列表顺便用* 号脱去中括号
print('字符为：',*zifu)
print('数字为：',*shuzi)
print('汉字为：',*hanzi)

import