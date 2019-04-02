d = {"name": '华华', 'hobby': '学Python', 'age': 18, 'score': {'en': 120, 'math': 99.99, 'ch': 'A'},
     'friend': ['bay max', '小CC', '如意'], True: 'good_man', 0.02: 'python', False: '这个value对应的key是布尔值',
     (1, 2, 3): '我就是元组大大！！！', 0: '这是真爱呀', 1: 'socre is 99.9'}
print(d)
#输出存在的问题是：1：缺少了'这个value对应的key是布尔值'  2：缺少了'good_man'
#原因是：这两个值的key和后面的key为0/1重复了，在python里：True等于1  false等于2