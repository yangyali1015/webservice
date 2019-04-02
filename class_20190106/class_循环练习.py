#
# a=('请输入您想要的配料：')
# active=True
# while active:
#     message =input(a)
#     if message =='quit':
#        active=False
#     else:
#       print('我们会在披萨中添加此配料')

# a='请问你多大了？'
# age =()
# while True:
#     age=int(input(a))
#     if age <=  3:
#         print('免费')
#     elif 3< age<12:
#         print('请支付10美元')
#     else:
#         print('请支付15美元')

# sandwich_orders=['汉堡包','肯德基','麦当劳','pastrami','pastrami','pastrami']
# finished_sandwiches=[]
# for name in sandwich_orders:
#     print('I made your' +name+'sandwich')
#     finished_sandwiches.append(name)
# print(finished_sandwiches)
# print('牛肉卖完了')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

dreams={}
active = True
while active:
    name = input ('您好，请问您怎么称呼？')
    dream = input ('请问你有什么梦想吗')
    dreams[name]=dream
    repeat = input('还要继续调查吗')
    if repeat == 'no':
        active =False
print('调查结果')
print(dreams)
for name,dream in dreams.items():
    print(name +'的梦想是：'+dream)




    # c[0] = {'手撕包菜': '10元', '香干肉丝': '10元', '土豆丝': '10元', '胡萝卜炒肉': '10元'}
    # c[1] = {'凉拌黄瓜': '10元', '凉拌皮蛋': '10元'}
    # c[2] = {'大盆花菜': '16元', '红烧鱼块': '18元'}
    # if order ==c[0]:
    #     for d in c :
    #         print(d)
    #        # for e in d.keys():
    #             f =input(('请输入菜名'))
    #             if f in e:
    #                 print(f +d[e])



    # 第二种方法
    # orders ={'手撕包菜':'10元','香干肉丝':'10元'}
    # a= input('输入菜名')
    # for b in orders .keys():
    #     c=[b]
    # if a ==b:
    #          print(a+orders[b])
    # elif a!=b:
    #        print('您要的菜我们店没有')

    # d=input('请选择您要的菜名')
    # if d== caiming:
    #     print(d+pingjia_orders[caiming])











