import pandas as pd
import sqlite3
import os

# 1. 读取清洗后的 .csv 文件
csv_path = r"C:\Users\GTF\Desktop\HTML\project\data\city_districts_clean.csv"
districts = pd.read_csv(csv_path)

# 2. 连接数据库，若不存在会自动创建
db_path = r"C:\Users\GTF\Desktop\HTML\project\database\surveillance.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 3. 用 SQL 创建 City Districts 表
cursor.execute("""
CREATE TABLE IF NOT EXISTS Districts (
    district_id TEXT PRIMARY KEY,
    district_name TEXT NOT NULL
);
""")

# 4. 清空已有数据（保险操作，避免重复导入）
cursor.execute("DELETE FROM Districts;")

# 5. 将数据逐条写入数据库
for _, row in districts.iterrows():
    cursor.execute("""
    INSERT INTO Districts (district_id, district_name)
    VALUES (?, ?);
    """, (row['district_id'], row['district_name']))

# 6. 提交更改，关闭连接
conn.commit()
conn.close()

print(f"数据库已成功创建，文件位置：{db_path}")
