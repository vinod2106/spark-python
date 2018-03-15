from sqlalchemy.sql import select
from connect_db import ConnectDb
class InsertDb(ConnectDb):

    def __init__(self):
        engine = self.engine
        self.conn = engine.connect()
        self.users_table = self.users_table

    def insert(self):
        self.conn.execute(self.users_table.insert(), [
        {"name": "Ted", "age":10, "password":"dink"},
        {"name": "Asahina", "age":25, "password":"nippon"},
        {"name": "Evan", "age":40, "password":"macaca"}
    ])

    def select(self):
        s = select([self.users_table])
        result = s.execute()
        for row in result:
            print("row: ", row)

if __name__ == '__main__':
    ins = InsertDb()
    ins.insert()
    ins.select()