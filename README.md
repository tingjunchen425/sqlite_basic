# Sqlite_Basic
## sqlite基礎資料庫應用

### 簡述
- 簡易的資料庫操作
- SQL指令查詢及生成

### 系統需求(建議)
python 3.11

### 檔案操作
- 克隆專案
`git clone https://github.com/tingjunchen425/sqlite_basic.git`
- 安裝相依套件
`pip install -r requirements.txt`
- 匯出資料庫(.db > .sql)
`sqlite3 my_database.db '.dump' > my_database.sql`
>[!Tips]補充說明
>- 記得將`my_database`換成自己的資料庫名稱

### 檔案介紹
#### [版本紀錄](https://github.com/tingjunchen425/sqlite_basic/blob/main/changeLog.md)
#### [資料庫相關功能](https://github.com/tingjunchen425/sqlite_basic/blob/main/db.py)
#### [sql指令相關功能](https://github.com/tingjunchen425/sqlite_basic/blob/main/sql.py)
#### [相依套件目錄](https://github.com/tingjunchen425/sqlite_basic/blob/main/requirements.txt)

### 功能說明
#### `db.py`
##### `class DB`
- 需輸入`db_name`進行初始化
- `db_name`的檔案類別需為`.db`檔
- 如果沒有對應的`.db`檔則會自動新增
##### `DB.close()`
- 關閉資料庫
##### `DB.create_table()`
- 創建資料表
- 需求輸入：
    - `name`：欲創建的資料表名稱
    - `columns_set`：資料表格式設定
        - ex ```column = """
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            """ ```
##### `DB.get_table_schema()`
- 查詢資料表格式設定
- 需求輸入：
    - `name`：欲查詢的資料表名稱
##### `DB.get_table_list()`
- 查詢所有資料表名稱及格式設定
##### `DB.drop_table()`
- 刪除資料表
- 需求輸入：
    - `name`：欲刪除的資料表名稱
##### `DB.operate()`
- 自行輸入SQL指令進行操作
- 需求輸入：
    - `sql`：SQL指令
##### `DB.Select()`
- 查詢資料表內容
- 需求輸入(可選)：
    1. `table`：通過輸入資料表名稱進行查詢
    2. `sql`：自行輸入SQL指令進行查詢
##### `DB.Insert()`
- 新增內容
- 需求輸入：
    - `name`：資料表名稱
- 會通過`sql.py`中的`SQL.Insert()`來生成SQL指令
##### `DB.Update()`
- 修改內容
- 需求輸入：
    - `name`：資料表名稱
- 會通過`sql.py`中的`SQL.Update()`來生成SQL指令
##### `DB.Delete()`
- 修改內容
- 需求輸入：
    - `name`：資料表名稱
- 會通過`sql.py`中的`SQL.Delete()`來生成SQL指令