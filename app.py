from flask import Flask, render_template, request, jsonify
import sqlite3
import time
import os

app = Flask(__name__)

# 路径配置，避免混乱
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "surveillance.db")
TRACKING_LOG = os.path.join(BASE_DIR, "tracking.log")

# ===== 数据功能部分 =====
def get_camera_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = """
    SELECT camera_id, location, power, type, vri_number, year, city_districts.district_name
    FROM camera_locations
    JOIN city_districts ON camera_locations.district_id = city_districts.district_id
    """
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in data]

def get_camera_locations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = """
    SELECT camera_id, location, district_id
    FROM camera_locations
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    # 虚拟经纬度
    cameras = []
    base_lat, base_lon = 52.3702, 4.8952
    for idx, row in enumerate(data):
        cameras.append({
            'camera_id': row[0],
            'location': row[1],
            'district_id': row[2],
            'lat': base_lat + 0.005 * idx,
            'lon': base_lon + 0.005 * idx
        })
    return cameras

# ===== 页面路由部分 =====
@app.route('/')
def home():
    log_tracking('home')
    return render_template('index.html')

@app.route('/data')
def data_page():
    log_tracking('data')
    return render_template('data.html', cameras=get_camera_data())

@app.route('/map')
def map_page():
    log_tracking('map')
    return render_template('map.html', cameras=get_camera_locations())

# ===== 自定义追踪功能部分 =====
def log_tracking(page_name):
    with open(TRACKING_LOG, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Page View: {page_name}\n")

@app.route('/track_time', methods=['POST'])
def track_time():
    data = request.get_json()
    with open(TRACKING_LOG, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Time on {data['page']}: {data['timeSpent']} seconds\n")
    return '', 204

@app.route('/track_map_click', methods=['POST'])
def track_map_click():
    with open(TRACKING_LOG, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Map marker clicked\n")
    return '', 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render会自动传入PORT
    app.run(host="0.0.0.0", port=port)