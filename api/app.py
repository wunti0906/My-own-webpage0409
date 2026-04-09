import os
from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

@app.route('/')
def index():
    data = {
        "name": "林彣媞",
        "student_id": "411312537",
        "class": "資管二B",
        "photos": ["photo.jpeg", "photo4.jpeg", "photo3.jpeg"],
        "slides_text": [
            "夢想如果不付諸行動，永遠都只是一種空想與幻想。",
            "請在此為自己提供一個實踐夢想行動的動力。",
            "讓夢想可以被實現。"
        ]
    }
    return render_template('index.html', info=data)

@app.route('/intro')
def intro():
    person_info = {
        "name": "林彣媞",
        "department": "資訊管理學系",
        "class": "資管二B",
        "student_id": "411312537",
        "email": "wunti0906@gmail.com",
        "skills": ["Python", "Flask", "網頁設計", "資料分析"],
        "bio": "目前就讀靜宜資管系，原本對 PM 感興趣，現在致力於深化技術，轉向後端工程師之路。"
    }
    return render_template('intro.html', person=person_info)

@app.route('/holland')
def holland():
    holland_data = {
        "name": "林彣媞",
        "date": "2024/05/20",
        "code": "ECI",
        "types": ["企業型", "事務型", "研究型"],
        "top_clusters": [
            {"name": "企業管理", "score": 7.0, "pr": 85},
            {"name": "資訊技術", "score": 6.0, "pr": 78},
            {"name": "財務金融", "score": 6.0, "pr": 75},
            {"name": "行銷企劃", "score": 5.5, "pr": 70}
        ]
    }
    return render_template('holland.html', data=holland_data)

@app.route('/future')
def future():
    wanin_data = {
        "company_name": "網銀國際股份有限公司",
        "industry": "遊戲軟體研發 / 數位內容 / 科技創新",
        "focus_areas": ["行動遊戲開發", "電競賽事發展", "第三方支付應用", "區塊鏈技術應用"],
        "philosophy": "科技創新、永續經營、回饋社會"
    }
    return render_template('future.html', wanin=wanin_data)

@app.route('/list2026')
def list2026():
    goals = [
        {"title": "雅思 (IELTS) 檢定", "desc": "達到平均 7.0 分以上，為出國交換或進修做準備。", "status": "準備中"},
        {"title": "看100本書籍", "desc": "廣泛閱讀提升知識廣度與深度，達成一年內閱讀 100 本書籍的目標。", "status": "計畫中"},
        {"title": "實習", "desc": "尋找軟體開發實習，累積實際專案撰寫經驗。", "status": "待執行"}
    ]
    return render_template('list2026.html', goals=goals)

@app.route('/career')
def career():
    career_info = {
        "title": "資管人的研發之路：邁向軟體工程師",
        "target_company": "網銀國際 (Wanin Industries)",
        "connection_points": [
            {"topic": "數據與後端架構", "desc": "資管系的資料庫管理與網銀的遊戲伺服器穩定性息息相關。"},
            {"topic": "數位金融與支付", "desc": "網銀支付系統是資管系金融科技課程的最佳實踐場景。"},
            {"topic": "技術開發的決心", "desc": "從理解業務邏輯轉向親手撰寫穩定代碼的後端工程師。"}
        ]
    }
    return render_template('career.html', career=career_info)

if __name__ == '__main__':
    app.run(debug=True, port=5001)