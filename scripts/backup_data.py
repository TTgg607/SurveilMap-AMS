import sqlite3
import pandas as pd
import os

db_path = os.path.join("..", "database", "surveillance.db")
conn = sqlite3.connect(db_path)

# 备份 camera_locations 表
camera_df = pd.read_sql_query("SELECT * FROM camera_locations;", conn)
camera_df.to_csv("../data/camera_locations_backup.csv", index=False)

# 备份 city_districts 表
districts_df = pd.read_sql_query("SELECT * FROM city_districts;", conn)
districts_df.to_csv("../data/city_districts_backup.csv", index=False)

conn.close()
print("数据备份完成，保存在 data 文件夹。")
