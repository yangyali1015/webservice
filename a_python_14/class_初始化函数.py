class Phone:
    #初始化函数__init__()
    def __init__(self,name,price,os,color,size):
        self.name=name#赋值给对象属性方便日后调用
        self.price=price
        self.os=os
        self.color=color
        self.size=size
    # name='oppo'#类的属性/类的变量
    # price=4500
    # os='android'
    # color='black'
    # size='5.5'
    #功能  类的函数
    def call(self):
        print('他可以打电话')
    def send_message(self):
        print('发短信')
    def watch_vedio(self):
        print('看电视')
    def take_shot(self):
        print('拍照')
    @classmethod
    def music(self):
        print('听歌')
#创建对象   对象拥有类里面所有属性和方法的访问权，访问全部
#如果你用了初始化函数，那么你在创建对象的时候必须要传参