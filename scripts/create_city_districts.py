import sqlite3
import pandas as pd
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "database", "surveillance.db")
data_path = os.path.join(project_root, "data", "city_districts_clean.csv")

df = pd.read_csv(data_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS city_districts (
    district_id TEXT PRIMARY KEY,
    district_name TEXT
);
""")

conn.commit()
df.to_sql("city_districts", conn, if_exists="append", index=False)

conn.close()
print("city_districts 表已重建并导入数据。")
