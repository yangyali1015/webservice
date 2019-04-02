#类的继承  apple  通过手机量身高
# from a_python_14.class_初始化函数 import  Phone
# class Applephone(Phone):
#     '''这是一个苹果类'''
#     @classmethod
#     def ceju(self):
#         print('可以测距离')
# #子类具有父类的所有方法和属性
# Applephone.music()
# #静态方法直接用类调用的时候不需要传参数，直接调用
# #父类里面又初始化函数的时候，子类创建对象的时候一定要传参数，除非他有默认值
# Applephone().ceju()

class Haha():
    def __init__(self,b):
        self.b=b
        self.a=12
    def maya(self):
        print(self.a+3)
c=Haha(2)
c.a=20
c.maya()
