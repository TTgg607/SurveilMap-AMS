import sqlite3
import pandas as pd
import os

db_path = os.path.join("..", "database", "surveillance.db")
conn = sqlite3.connect(db_path)

# 恢复 city_districts
districts_df = pd.read_csv("../data/city_districts_backup.csv")
districts_df.to_sql("city_districts", conn, if_exists="append", index=False)

# 恢复 camera_locations
camera_df = pd.read_csv("../data/camera_locations_backup.csv")
camera_df.to_sql("camera_locations", conn, if_exists="append", index=False)

conn.close()
print("数据恢复完成。")
