import sqlite3
import pandas as pd
import os

project_root = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(project_root, "database", "surveillance.db")

conn = sqlite3.connect(db_path)

print("\n=== camera_locations 表内容 ===")
df_camera = pd.read_sql_query("SELECT * FROM camera_locations;", conn)
print(df_camera.head(10))

print("\n=== city_districts 表内容 ===")
df_district = pd.read_sql_query("SELECT * FROM city_districts;", conn)
print(df_district.head(10))

print("\n=== 联结查询结果 ===")
df_join = pd.read_sql_query("""
SELECT camera_id, location, power, type, vri_number, year, city_districts.district_name
FROM camera_locations
JOIN city_districts ON camera_locations.district_id = city_districts.district_id;
""", conn)
print(df_join.head(10))

conn.close()

