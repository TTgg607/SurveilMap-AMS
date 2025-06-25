import pandas as pd
import os

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "camera_data_final.csv")
clean_path = os.path.join(project_root, "data", "camera_locations_clean.csv")

# 读取数据
df = pd.read_csv(data_path)

# 清洗数据
df['camera_id'] = df['camera_id'].str.strip()
df['Soort'] = df['Soort'].str.strip()
df['Standplaats'] = df['Standplaats'].str.strip()
df['Bouwjaar'] = df['Bouwjaar'].astype(str).str.strip()
df['Voeding'] = df['Voeding'].str.strip()
df['VRI number'] = df['VRI number'].astype(str).str.strip()
df['VRI number'] = df['VRI number'].str.replace('-', '', regex=False)

# 重命名字段
df_clean = df.rename(columns={
    'camera_id': 'camera_id',
    'Soort': 'type',
    'Standplaats': 'location',
    'Bouwjaar': 'year',
    'Voeding': 'power',
    'VRI number': 'vri_number'
})

# 定义映射逻辑
def map_location_to_district(location):
    if "Verlengde Stellingweg" in location:
        return "A"
    elif "IJdoornlaan" in location:
        return "M"
    elif "Nieuwe Leeuwarderweg" in location:
        return "M"
    elif "Zuiderzeeweg" in location:
        return "M"
    elif "Haarlemmerweg" in location:
        return "B"
    else:
        return None

df_clean['district_id'] = df_clean['location'].apply(map_location_to_district)

# 保存清洗结果
df_clean.to_csv(clean_path, index=False)
print(f"\n清洗后的数据已保存至：{clean_path}")
