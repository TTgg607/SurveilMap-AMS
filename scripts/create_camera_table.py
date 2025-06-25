import sqlite3
import pandas as pd
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "database", "surveillance.db")
data_path = os.path.join(project_root, "data", "camera_locations_clean.csv")

df = pd.read_csv(data_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS camera_locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    camera_id TEXT,
    district_id TEXT,
    location TEXT,
    power TEXT,
    type TEXT,
    vri_number TEXT,
    year INTEGER,
    FOREIGN KEY (district_id) REFERENCES city_districts(district_id)
);
""")

cursor.execute("DELETE FROM camera_locations")

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO camera_locations (camera_id, district_id, location, power, type, vri_number, year)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        row['camera_id'],
        row['district_id'],
        row['location'],
        row['power'],
        row['type'],
        row['vri_number'],
        row['year']
    ))

conn.commit()
conn.close()
print("摄像头数据已成功写入数据库！")
