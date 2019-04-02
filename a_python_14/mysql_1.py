from mysql import connector
# 第一步：链接数据库
# 提供数据库的连接信息
db_config={'host':'47.107.168.87','user':'python','password':'python666','port':3306,'database':'future'}


#建立连接
cnn=connector.connect(**db_config)

#第二步  ：获取游标  获取操作数据库的权限
cursor=cnn.cursor()

#第三步操作数据表
query='select * from member where Mobilephone=13755127762'
cursor.execute(query)

#第四步  获取查询的结果并且打印结果
res_1= cursor.fetchall()#打印符合条件的所有数据
res_2=cursor.fetchone()#打印第一条
#如果先执行打印全部那么打印第一条的没有数据
#如果限制性打印第一条那么打印全部只会打印剩下的
print(res_1)

#以上是进行数据库的查
#如果是进行数据库的增删改  就不需要第四步   把第四步换成
cursor.execute('commit')