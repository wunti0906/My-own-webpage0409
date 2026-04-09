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

@app.route('/intro')
def intro():
    person_info = {
        "name": "林彣媞",
        "department": "資訊管理學系",
        "class": "資管二B",
        "student_id": "411312537",
        "email": "wunti0906@gmail.com",
        "skills": ["Python", "Flask", "網頁設計", "資料分析"],
        "bio": "目前就讀靜宜資管系，對於專案管理與後端開發充滿興趣，致力於成為一名優秀的專案經理 (PM)。"
    }
    return render_template('intro.html', person=person_info)

@app.route('/future')
def future():
    wanin_data = {
        "company_name": "網銀國際股份有限公司",
        "industry": "遊戲軟體研發 / 數位內容 / 科技創新",
        "focus_areas": ["行動遊戲開發", "電競賽事發展", "第三方支付應用", "區塊鏈技術應用"],
        "philosophy": "科技創新、永續經營、回饋社會",
        "career_connection": "作為資管系學生，網銀國際提供的技術開發、數據分析與專案管理職位是完美的職涯接軌目標。"
    }
    return render_template('future.html', wanin=wanin_data)

@app.route('/list2026')
def list2026():
    goals = [
        {"title": "雅思 (IELTS) 檢定", "desc": "達到平均 7.0 分以上，為出國交換或進修做準備。", "status": "準備中"},
        {"title": "考取汽車駕照", "desc": "完成駕訓班課程並取得駕照，提升生活移動的便利性。", "status": "計畫中"},
        {"title": "專案管理實習", "desc": "尋找與 PM 相關的實習機會，累積實務經驗。", "status": "待執行"}
    ]
    return render_template('list2026.html', goals=goals)

if __name__ == '__main__':
    # 這裡使用 5001 埠號以避開 Mac 系統衝突
    app.run(debug=True, port=5001)