# 关键字是dic dictionary
# 特征是{}
# {}括起来的都是字典 看类型 type
# 空字典d={}
# 字典里面
#字典里面元素存储的方式key：value的形式键值对
#key不可变，唯一

#字典，是一系列的键值对
#每个键 键 都与一个值相关联，你可以使用键来访问与之相关联的值。
#与键相关联的值可以是数字、字符串、列表乃至字典
#字典用花括号表示{}
#键 键—值 值 对是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔
#键值与键值之间用逗号分隔
# a={'name':'xiaoming','score':60}
# 字典里查询只能搜索键名，但是如果字典里有列表可以嵌入先查询键值对然后再查询列表里的索引
# #添加键值对，指定字典名、用方括号括起的键和相关联的值。 例如
# a['wahaha'] = 5
# print(a)
# #修改字典里的值 直接提取出键名等于什么例如
# a['wahaha']=6
# print(a)
# #多行字典
# names={'xiaoming':5,
#        'xiaozhang':6,
#        }
# a=names['xiaoming']
# print('我最喜欢的数字是'+str(a))
# #便利字典里的键值，可以是键也可以是值，也可以是键值
# users={'name':'xiaoming','shengao':'hengao'}
# for key , value in users.items():
#     print(key)
#     print(value)
# #如果想要对字典里的key进行排序可以使用sorted,输出的按照字母进行排序
# 运用for循环时
# for 变量  in  sorted 原变量 :
# 在进行for循环时如果提取的量很大，为了避免重复
# 我们可以使用集合（set)
# for 变量  in  set  原变量 :
# fovorite_lanjuage={'xiaoming':'yuwen','xiaohong':'yingyu','xiaofang':'shuxue','xiaojun':'shuxue'}
# a=['shuxue']
# for language in fovorite_lanjuage.values():
#     if language in a:
#         print('我最喜欢的科目是：'+language)
#     if language not in a :
#         print('我一点也不喜欢'+language)
# if 'huaxue' not in fovorite_lanjuage.values():
#         print('其实我也很喜欢'+'huaxue')
# print('这是我学过的所有科目:')
# for language in set (fovorite_lanjuage .values()):
#     print(language.title())
# a=[]
# for b in range(5):
#     c={'xiaoming':'shuxue','xiaohong':'yuwen'}
#     a.append(c)
# for haha in a[:3]:
#          print(haha)
# print(str(len(a)))
names=[]
for name_number in range (0,10):
    new_name={'clor':'green','age':20,'speed':'slow'}
    names.append(new_name)
for name in names[0:5]:
    if name['clor'] =='green':
         name['clor']='yellow'
         print(name)

# d={}
# print(type(d))
d={"name":"执着","hobby":"学python","age":18}
print(d)
#取值的时候是按照Key取值不是按照索引取值，也就是取值的时候必须写下里面是什么内容，不可以写这是第几个索引
#支持增删改
d['salary']="20k"  #不存在里面的key就是新增，存在的话就是修改
print(d)
# 删除 根据key去删除d.pop("friend")指定删除
d.popitem()#随机删除

# messages={'names':'xiaoming','shengao':178,'height':65.6}
# numbers={'小明':1,'小红':2,'小芳':3,'小黑':4,'小白':5}
# for key,value in numbers.items():
#     print(key+'喜欢'+str(value))
# names=['小红','小萌','校长','小芳']
# aiya={'1号':'小红','2号':'小明'}
# for name in names:
#     if name in aiya.values():
#         print('感谢'+name)
#     else:
#         print('再见'+name)
#
# dog={'name':'小灰灰','主人':'鸭梨','身高':166}
# cat={'name':'小裙子','主人':'晶晶','身高':168}
# pets=[{'name':'小灰灰','主人':'鸭梨','身高':166},{'name':'小裙子','主人':'晶晶','身高':168}]
# for pet in pets:
#     print(pet)

favorite_place ={'晶晶':['河南','海南','武汉'],'灰灰':['深圳','广州','武汉'],'裙子':['蕲春','武汉','江苏']}
for name , place in favorite_place.items():
    print(name , place )