import pandas as pd

# 明确路径，使用原始数据文件
data_path = r"C:\Users\GTF\Desktop\HTML\project\data\INDELING_STADSDEEL.csv"

# 读取数据，注意荷兰数据通常用分号分隔
districts = pd.read_csv(data_path, sep=';')

# 查看前几行，确认结构（可选）
print("原始数据前几行：")
print(districts.head())

# 只保留需要的字段
districts_clean = districts[['Stadsdeelcode', 'Stadsdeel']].copy()

# 重命名字段，更符合数据库规范
districts_clean.rename(columns={
    'Stadsdeelcode': 'district_id',
    'Stadsdeel': 'district_name'
}, inplace=True)

# 删除缺失值
districts_clean.dropna(subset=['district_id', 'district_name'], inplace=True)

# 删除重复值
districts_clean.drop_duplicates(subset=['district_id'], inplace=True)

# 重置索引
districts_clean.reset_index(drop=True, inplace=True)

# 显示清洗后的结果
print("\n清洗后的数据：")
print(districts_clean)

# 保存清洗后的数据
output_path = r"C:\Users\GTF\Desktop\HTML\project\data\city_districts_clean.csv"
districts_clean.to_csv(output_path, index=False)

print(f"\n清洗后的数据已保存至：{output_path}")
