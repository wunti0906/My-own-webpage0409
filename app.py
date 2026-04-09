from flask import Flask, render_template

app = Flask(__name__)

# --- 路由 1：首頁 ---
@app.route('/')
def index():
    # 這裡存放要傳送到 index.html 的首頁資訊
    info_data = {
        "name": "林彣媞",
        "student_id": "411312537",
        "class": "資管二B",
        # 輪播圖照片清單 (對應 static 資料夾內的檔名)
        "photos": ["photo.jpeg", "photo4.jpeg", "photo3.jpeg"],
        # 輪播圖對應的文字
        "slides_text": [
            "夢想如果不付諸行動，永遠都只是一種空想與幻想。",
            "請在此為自己提供一個實踐夢想行動的動力。",
            "讓夢想可以被實現。"
        ]
    }
    return render_template('index.html', info=info_data)

# --- 路由 2：何倫碼 / UCAN 診斷結果頁 ---
@app.route('/holland')
def holland():
    # 這裡存放 UCAN 診斷的詳細資料
    ucan_data = {
        "name": "林彣媞",
        "date": "2024年09月02日",
        "code": "ECI",
        "types": ["企業型 (E)", "事務型 (C)", "研究型 (I)"],
        "top_clusters": [
            {"name": "企業經營管理", "score": "3.80", "pr": "96"},
            {"name": "教育與訓練", "score": "3.80", "pr": "91"},
            {"name": "醫療保健", "score": "3.80", "pr": "95"},
            {"name": "司法、法律與公共安全", "score": "3.20", "pr": "84"}
        ]
    }
    # 將資料傳送到 holland.html，變數名稱設為 data
    return render_template('holland.html', data=ucan_data)

# --- 路由 3：自我介紹詳細頁 (可選) ---
@app.route('/intro')
def intro():
    return "<h1>自我介紹詳細內容</h1><p>這裡是林彣媞的詳細自我介紹頁面。</p><a href='/'>返回首頁</a>"

# --- 路由 4：未來規劃詳細頁 (可選) ---
@app.route('/future')
def future():
    return "<h1>未來規劃詳細內容</h1><p>目標職位：專案經理 (PM)。</p><a href='/'>返回首頁</a>"

# --- 路由 5：2026 清單詳細頁 (可選) ---
@app.route('/list2026')
def list2026():
    return "<h1>2026 願望清單</h1><p>1. 完成資管專題<br>2. 考取證照</p><a href='/'>返回首頁</a>"

if __name__ == '__main__':
    # debug=True 可以在你修改程式碼存檔後，讓伺服器自動重新啟動
    app.run(debug=True)
