from db import DB
from sql import SQL

database = 'test.db'
db = DB(database)
sql = SQL(database)

column = """
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL
"""

# db.create_table('users',column)

# sql = "INSERT INTO users (id,name,password) VALUES ('A001','administrator','124592376')"
# db.operate(sql)

# db.get_table_schema('users')
# db.get_table_list()
# db.Select('users')
# db.Update('users')
# db.Select('users')
# db.Delete('users')
# db.Select('users')
# db.Insert('users')
# db.Select('users')
# db.create_table('test',column)
# db.get_table_list()
# print('-'*40)
# db.get_table_schema('test')
# db.drop_table('test')
db.get_table_list()
db.Select('users')
db.close()