import sqlite3
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "database", "surveillance.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS camera_locations;")
cursor.execute("DROP TABLE IF EXISTS city_districts;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS city_districts (
    district_id TEXT PRIMARY KEY,
    district_name TEXT
);
""")

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

conn.commit()
conn.close()
print("新表已重建完成，外键结构已正确声明。")
