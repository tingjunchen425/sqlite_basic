import sqlite3


class SQL:
    def __init__(self,db_name):
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print('Error: ', e)
    
    def close(self):
        if self.conn:
            self.conn.close()

    def Insert(self,name):
        try:
            self.cursor.execute(f"PRAGMA table_info({name})")
            rows = self.cursor.fetchall()
            schema = []
            for row in rows:
                schema.append([row[1],row[2]])
            key = ""
            for i in schema:
                key += i[0] + ","
            key = key[:-1]
            value = ""
            for i in schema:
                v = input(f"{i[0]}({i[1]}): ")
                if i[1] == 'TEXT':
                    v = f"'{v}'"
                value += v + ","
            value = value[:-1]
            sql = f"INSERT INTO {name} ({key}) VALUES({value})"
            print(sql)
            return sql
        except sqlite3.Error as e:
            print('Error: ', e)

    def Select(self,name,key,value):
        try:
            self.cursor.execute(f"SELECT * FROM {name} where {key} = '{value}'")
            rows = self.cursor.fetchall()
            row = list(rows[0])
            return row
        except sqlite3.Error as e:
            print('Error: ', e)
    
    def Select_key(self,name,key):
        try:
            self.cursor.execute(f"SELECT {key} FROM {name}")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print('Error: ', e)

    def Update(self,name):
        try:
            self.cursor.execute(f"PRAGMA table_info({name})")
            rows = self.cursor.fetchall()
            schema = []
            for row in rows:
                schema.append([row[1],row[2]])
            key = ""
            for i in schema:
                key += i[0] + ","
            key = key[:-1]
            value = ""
            key = input(f"Key({key}): ")
            print(self.Select_key(name,key))
            key_value = input(f"Key Value: ")
            db_value = self.Select(name,key,key_value)
            print(db_value)
            for i in schema:
                v = input(f"{i[0]}({i[1]}): {db_value[schema.index(i)]}(若不更改請按enter) -> ")
                if v == "": v = db_value[schema.index(i)]
                if i[1] == 'TEXT':
                    v = f"'{v}'"
                value += i[0] + "=" + v + ","
            value = value[:-1]
            sql = f"UPDATE {name} SET {value} WHERE {key} = '{key_value}'"
            print(sql)
            return sql
        except sqlite3.Error as e:
            print('Error: ', e)
        
    def Delete(self,name):
        try:
            table_info = self.cursor.execute(f"PRAGMA table_info({name})").fetchall()
            info = []
            for i in table_info:
                info.append(i[1])
            print(info)
            key = input("Key: ")
            print(self.Select_key(name,key))
            value = input("Value: ")
            sql = f"DELETE FROM {name} WHERE {key} = '{value}'"
            print(sql)
            return sql
        except sqlite3.Error as e:
            print('Error: ', e)
            