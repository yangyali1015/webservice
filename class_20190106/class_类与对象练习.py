# class Dog():
#     def __init__(self,name,shengao):
#         self.name=name
#         self.shengao=shengao
#     def sit(self):
#         print('正在跳'+ str(self.shengao))
#     def rollover(self):
#         print('正在滚')
# peiqi=Dog('peiqi',175)
# peiqi.shengao=180
# peiqi.sit()
# peiqi.rollover()
# #括号里的name等叫做属性，访问属性是实例名.属性   例如  peiqi.name
# class Dog_1(Dog):
#     def __init__(self,name,shengao):
#          super().__init__(name,sheng
# from random import randint
# # a=randint(1,8)
# # print(a)
# class Die():
#     def __init__(self,sides):
#         self.sides=6
#     def roll_die(self):
#         # a=randint(1,self.sides)
#         b=0
#         while b<self.sides :
#             a = randint(1, self.sides)
#             b=b+1
#             print(a)
# b=Die(6)
# b.roll_die()

class Dog :
    a=2
    b=3

    @classmethod
    def add(cls):
        print(Dog(cls.a+cls.b))

class Dog_1(Dog):
    def add(self):
        print(self.a-self.b)

Dog_1().add()
