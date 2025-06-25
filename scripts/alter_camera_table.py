import sqlite3
import os

# 数据库路径
db_path = os.path.join("..", "database", "surveillance.db")

# 连接数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 给 camera_locations 表新增 district_id 字段
cursor.execute("""
ALTER TABLE camera_locations ADD COLUMN district_id TEXT;
""")

conn.commit()
conn.close()

print("字段 district_id 已成功添加到 camera_locations 表。")
