from flask import render_template
from sqlalchemy import desc
import requests
from application.models import history
from application import app, db

@app.route('/')
def index():
    rarity = requests.get('http://service_2:5002/get/rarity').text
    gun = requests.get('http://service_3:5003/get/gun').text

    payload = {'rarity':rarity, 'gun':gun}
    price = requests.get('http://service_4:5004/post/winnings', json=payload).json()

    rollhistory = history.query.order_by(desc(history.id)).limit(5).all()

    storeroll = history(rarity=rarity, gun=gun)
    db.session.add(storeroll)
    db.session.commit()


    return render_template("main.html",storeroll = storeroll, rollhistory = rollhistory, price=price)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)