#1：编写一个数学类，要求初始化函数带a,b,c,d4个参数，然后有加减乘数四个函数
# class Math:
#     '''这是一个数学类，可以进行加减乘除运算'''
#     def __init__(self,a,b,c,d):#定义一个初始化函数，有四个形参
#         self.a=a#将初始化函数的属性赋值给对象的属性
#         self.b=b
#         self.c=c
#         self.d=d
#     def add(self):#加法
#         e=self.a+self.b
#         return e
#     def sub(self):#减法
#         f=self.c-self.d
#         return f
#     def multiply(self):#乘法
#         i=self.a*self.b
#         return i
#     def divide(self):#除法
#         g=self.c/self.d
#         return g
# if __name__=='__main__':#主函数
#     math_1=Math(1,2,3,4)#创建一个实例
#     print(math_1.add())#调用类里面方法
#     print(math_1.sub())
#     print(math_1.multiply())
#     print(math_1.divide())

#2：依靠自己的想象力，编写一个软件测试工程师类，要求包含初始化函数 类函数 对象函数  静态函数
class SoftwareTestingEngineer:
    '''这是一个软件测试工程师类'''
    def __init__(self,name,hair,skill):
        self.name=name#将初始化函数的属性赋值给对象
        self.hair=hair#头发数量
        self.skill=skill#技能
        SoftwareTestingEngineer.gender='女'#默认性别为女
    def outsight(self):
        print('{}拥有敏锐的观察力'.format(self.name))
    def skill_1(self):
        print('{},会{}'.format(self.name,self.skill))
    def hair_1(self):
        if self.hair==0:
            print('{}拥有的头发数量为{},ta是个秃子'.format(self.name,self.hair))
        else:
            print('{}拥有的头发数量为{},ta技能肯定不是很牛'.format(self.name, self.hair))
    def find_bug(self):
        print('{}可以发现程序的异常和错误。'.format(self.name))
    @classmethod
    def test_case(cls):
        print('你好，这个工程师会写测试用例哦,而且性别是{}'.format(SoftwareTestingEngineer.gender))
    @staticmethod
    def test_report():
        print('ta会写测试报告哦。')
if __name__=='__main__':#设置主函数入口
    a=SoftwareTestingEngineer('华华',0,'python自动化啊')
    print(a.name)
    a.outsight()
    a.skill_1()
    a.hair_1()
    SoftwareTestingEngineer.test_case()
    a.test_report()


