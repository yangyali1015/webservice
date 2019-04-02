import json
def greet():
    name_1='info3.json'
    try:
        with open(name_1) as name_2:
            name_3=json.load(name_2)
    except:
        info3=input('请输入用户名：')
        with open (name_1,'w') as name_4:
            json.dump(info3,name_4)
            print('我们将会存储您的姓名')
    else:
        print('欢迎回来！')

greet()