from flask import Flask, render_template

app = Flask(__name__)

# 首页
@app.route('/')
def home():
    return render_template('index.html')

# 地图页
@app.route('/map')
def map_page():
    return render_template('map.html')

# 数据页
@app.route('/data')
def data_page():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
