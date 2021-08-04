from flask import render_template
from sqlalchemy import desc
import requests
import datetime
from models import history
from . import app, db

@app.route('/')
def index():
    rarity = requests.get('http://service_2:5001/get/rarity').text
    gun = requests.get('http://service_3:5002/get/gun').text

    payload = {'rarity':rarity, 'gun':gun}
    price = requests.get('http://service_4:5003/post/winnings', json=payload).json()

    rollhistory = history.query.order_by(desc(history.id)).limit(5).all()

    storeroll = history(rarity=rarity, gun=gun)
    db.session.add(storeroll)
    db.session.commit()

    date = datetime(datetime.now().year, datetime.now().month,datetime.now().day)

    return render_template("main.html",storeroll = storeroll, rollhistory = rollhistory, date=date, price=price)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)