import sqlite3
from sql import SQL

class DB:
    def __init__(self,db_name):
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.sql = SQL(self.db_name)
        except sqlite3.Error as e:
            print('Error: ', e)

    def close(self):
        if self.conn:
            self.conn.close()
            self.sql.close()

    def create_table(self,name,columns_set):
        try:
            self.cursor.execute(f'''
                CREATE TABLE if not Exists {name}(
                    {columns_set}
                        )''')
            print("Table created successfully or already exists")
        except sqlite3.Error as e:
            print('Error: ', e)

    def get_table_schema(self,name):
        import pandas as pd
        from tabulate import tabulate
        try:
            self.cursor.execute(f"PRAGMA table_info({name})")
            rows = self.cursor.fetchall()
            schema = []
            for row in rows:
                row = list(row)
                if row[3] == 0:
                    row[3] = False
                else:
                    row[3] = True
                if row[5] == 0:
                    row[5] = False
                else:
                    row[5] = True
                rowlist = [row[0],row[1],row[2],row[3],row[4],row[5]]
                schema.append(rowlist)
            schema = pd.DataFrame(schema)
            schema.columns = ['cid','name','type','notnull','dflt_value','primary_key']
            schema.set_index('cid',inplace=True)
            title = f"Table: {name}"
            print(title.center(40,'-'))
            print(tabulate(schema, headers='keys', tablefmt='fancy_grid'))
        except sqlite3.Error as e:
            print('Error: ', e)

    def get_table_list(self):
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            rows = self.cursor.fetchall()
            tables = []
            for row in rows:
                tables.append(row[0])
            for table in tables:
                self.get_table_schema(table)
                print()
        except sqlite3.Error as e:
            print('Error: ', e)

    def drop_table(self,name):
        try:
            self.cursor.execute(f"DROP TABLE {name}")
            print("Table dropped successfully")
        except sqlite3.Error as e:
            print('Error: ', e)

    def operate(self,sql,type=""):
        try:
            if type == "insert":
                self.cursor.execute(sql)
                self.conn.commit()
                print("Insert success")
            elif type == "delete":
                self.cursor.execute(sql)
                self.conn.commit()
                print("Delete success")
            elif type == "update":
                self.cursor.execute(sql)
                self.conn.commit()
                print("Update success")
            else:
                self.cursor.execute(sql)
                self.conn.commit()
                print("Operation done successfully")
        except sqlite3.Error as e:
            print('Error: ', e)

    def Select(self,table="",sql="SELECT * FROM "):
        sql = sql + table
        if sql == "SELECT * FROM " and table == "":
            print("SQL error: No table specified")
            return
        import pandas as pd
        from tabulate import tabulate
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            schema = []
            for row in rows:
                row = list(row)
                schema.append(row)
            schema = pd.DataFrame(schema)
            if len(schema) == 0:
                print("No data found")
                return
            schema.columns = [i[0] for i in self.cursor.description]
            schema.set_index(schema.columns[0],inplace=True)
            title = f"Table: {table}"
            print(title.center(40,'-'))
            print(tabulate(schema, headers='keys', tablefmt='fancy_grid'))
            return rows
        except sqlite3.Error as e:
            print('Error: ', e)

    def Insert(self,name):
        try:
            sql = self.sql.Insert(name)
            self.operate(sql,type="insert")
        except sqlite3.Error as e:
            print('Error: ', e)

    def Update(self,name):
        try:
            sql = self.sql.Update(name)
            self.operate(sql,type="update")
        except sqlite3.Error as e:
            print('Error: ', e)

    def Delete(self,name):
        try:
            sql = self.sql.Delete(name)
            self.operate(sql,type="delete")
        except sqlite3.Error as e:
            print('Error: ', e)
    
