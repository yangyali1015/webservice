# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
#
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
from random import randint
class CaiQuan:
        def jiaose(self):#选择角色
            a={1:'曹操',2:'张飞',3:'刘备'}
            print('有如下几种角色:{}'.format(a))
            while True:
                print('编号如下：')
                for c in a:#遍历角色的key也就是序号
                    print(c,end='')#打印序号并且不换行
                try:#判断异常，防止用户输入非数字类型内容
                  b=int(input('\n请输入编号选择角色：'))#让用户输入编号
                except Exception as e:
                  print('输入有误，请重新输入！错误信息为：{}'.format(e))
                try:#判断异常
                    if b not in a.keys():#如果编号不等于字典里的编号就重新输入
                            print('请重新选择正确编号。')
                    elif b in a.keys():#如果等于就直接打印角色
                        print('您好，您选择的角色为：{}'.format(a[b]))
                        break
                except Exception as f:
                         print('输入有误，请重新输入！错误信息为：{}'.format(f))

        def jiaose_caiquan(self):#角色出拳
            i = {1: '剪刀', 2: '石头', 3: '布'}
            print('请出拳:{}'.format(i))
            while True:
                print('编号如下：')
                for j in i:#遍历出拳的编号
                    print(j, end='')  # 打印编号
                try:  # 判断异常，防止用户输入非数字类型内容
                    m = int(input('\n请输入编号出拳：'))  # 让用户输入编号
                except Exception as e:
                    print('输入有误，请重新输入！错误信息为：{}'.format(e))
                try:  # 判断异常
                    if m not in i.keys():  # 如果编号不在字典里的编号就重新输入
                        print('请重新选择正确编号。')
                    elif m in i.keys():  # 如果在就直接打印字典里对应编号的值
                        print('您好，您出的是：{}'.format(i[m]))
                        return m #返回的m用来后面和电脑的出拳作对比
                        break   #编号在里面就终止循环
                except Exception as f:
                    print('输入有误，请重新输入！错误信息为：{}'.format(f))


        def cmputer_1(self):#电脑出拳
            number=randint(1,3) #电脑出拳的编号为随机数1,2,3
            if number==1:
                print('电脑出拳为剪刀。')
            elif number==2:
                print('电脑出拳为石头。')
            else:
                print('电脑出拳为布。')
            return  number #返回的number用于后期和上面函数角色出拳结果作对比

        def fight(self):#这是一个对战的函数
            CaiQuan().jiaose() #首先让玩家选择角色，这个不需要进入循环
            win = 0  # 玩家赢的次数初始化为0
            while True:
                # self.jiaose_caiquan()#调用上面的角色出拳函数，让玩家开始出拳
                # self.cmputer_1()#调用上面的电脑出拳函数，让电脑开始出拳
                ren=CaiQuan().jiaose_caiquan()#此处打印的是角色出拳的结果编号，也就是角色出拳的返回值
                com=CaiQuan().cmputer_1()#此处打印的是电脑出拳的结果编号，也就是电脑函数的返回值
                if ren==com:#如果编号相等就是平局
                    print('平局')
                elif ren==1 and com==2 :#如果玩家出剪刀，电脑出石头
                    print('玩家输')
                elif ren==1 and com==3:#如果玩家出剪刀，电脑出布
                    print('玩家赢')
                    win+=1
                elif ren==2 and com==1:#如果玩家出石头，电脑出剪刀
                    print('玩家赢')
                    win += 1
                elif ren==2 and com==3:#如果玩家出石头，电脑出布
                    print('玩家输')
                elif ren==3 and com==1:#如果玩家出布，电脑出剪刀
                    print('玩家输')
                elif ren==3 and com==2:#如果玩家出布，电脑出石头
                    print('玩家赢')
                    win += 1
                try:
                    stop=input('请选择是否继续？按y继续，按n退出')
                except Exception as e:
                    print('请输入y或者n')
                if stop=='y':
                        continue
                elif stop =='n':
                    print('玩家赢的总次数为{}'.format(win))
                    break


if __name__=='__main__':
     CaiQuan().fight()

# 2：编写一个类：你们自行去设计，要求写一个类， 初始化函数 对象函数 包含 根据你不同的选择完成get请求 OR post请求 ，其中url 需要做参数化，并且最后要拿到响应结果
import requests#调用requests模块
# requests.get()
class HttpRequest():#编写一个可以进行get和post请求的类
    def __init__(self,url):#初始化函数
        self.url=url
        # self.username=username
        # self.password=password
    def get(self):#进行get请求
        print(requests.get(self.url))
        a = requests.get(self.url)
        print(a.text)#将响应结果打印出来
    def post(self):#进行post请求
        print(requests.post(self.url))
        a=requests.post(self.url)
        print(a.text)#将响应结果打印出来
if __name__=='__main__':
    zhanghu=HttpRequest('https://www.ketangpai.com/User/login.html')
    zhanghu.get()
    zhanghu.post()


