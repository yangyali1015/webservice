#类划分的标准是什么：具有相同特征或者相同行为的一类事物
#对象  类里面的一个具体事例
#编写手机类   特征/功能
#品牌名  价格
#打电话  发短信 看视频  玩游戏  拍照  听音乐  上网
#类的语法
#class ClassName:
 # '类的帮助信息' #类文档字符串
 #  class_suit#类体

#1/类体里面可以包含：类属性和类函数
#2/类名：见明知意
#3/创建一个对象/实例化
# 创建实例：a=类名（）#那么a就是一个对象
#对象：  创建对象：类名（）
#结论：类和对象都可以直接访问属性，并且获得他们的值
#类里面的方法：对象.方法名()
class Phone:
    name='oppo'#类的属性/类的变量
    price=4500
    os='android'
    color='black'
    size='5.5'
    #功能  类的函数
    def call(self):
        print('他可以打电话')

    def send_message(self):
        print('发短信')
    def watch_vedio(self):
        print('看电视')
    def take_shot(self):
        print('拍照')
    def music(self):
        print('听歌')


#对象调用：类名（）  和函数调用一样
# p=Phone()
#通过对象访问她的属性   对象.属性名
#结论：类和对象可以直接访问属性，并且获得他们的值（需要打印才显示出来
# p.name
# # p.price
# p.color

#访问方法   对象.方法名（）
#self 是什么东西，就是对象本身，只有对象才可以调用方法
# p.call()
#静态方法：@staticmethod放在函数上面，来标记和装饰，此时方法的括号内不要写self
#可以通过类以及对象来访问
#类方法：classmethod放在函数上面，来标记和装饰，此时的方法括号内要写一个cls
#可以通过类以及对象来访问

#类的方法和普通函数有啥区别呢
# 除了对象方法必须又self 类方法必须有cls   参数以外其他的并无区别
#参数类型：位置参数  默认参数  关键字参数  动态参数都有
#return
#

# 在python中首字母大写的名称指的是类例如：
# class Dog():  #此处定义了一个狗的类，狗的首字母是大写
#     def       #接下来定义这个类的函数
# class Dog():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def roll(self):
#         print('他会跳')
#     def sit(self):
#         print('他会坐')
# my_dog=Dog('xiaoming',18)
# my_dog.sit()#调用方法
# my_dog.roll()#调用方法

# class Restaurant():
#     def __init__(self,reataurant_name,cuisine_type):
#         self.reataurant_name=reataurant_name
#         self.cuisine_type=cuisine_type
#     def describe_restaurant(self):
#         print('这是一家名为',self.reataurant_name,'的餐厅')
#     def open_restaurant(self):
#         print('正在营业')
#
# my_restaurant=Restaurant('麦当劳','欧式')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# my_restaurant=Restaurant('肯德基','开放')
# my_restaurant.describe_restaurant()
# my_restaurant=Restaurant('海底捞','干净')
# my_restaurant.describe_restaurant()
#在创建子类时父类必须包含在当前文件夹中，定义子类时，父类必须再子类的括号中
# class Users():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def describe_user(self):
#         print('这是一个叫{}的人'.format(self.first_name+self.last_name))
#     def greet_user(self):
#         print('你好啊{}'.format(self.first_name+self.last_name))
# xiaoming=Users('xiao','ming')
# xiaoming.describe_user()
# xiaoming.greet_user()