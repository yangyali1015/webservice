from mysql import connector
class Mysql:
    def __init__(self,db_config,query):
        self.db_config=db_config
        self.query=query
    def select(self):
        cnn=connector.connect(self.db_config)
        cursor = cnn.cursor()
        cursor.execute(self.query)
        res_1 = cursor.fetchone()
        return res_1