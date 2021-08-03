from flask import Flask, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
import os
import datetime


app = Flask(__name__) # Creating Flask Object
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = str(os.urandom(16))



db = SQLAlchemy(app) # create SQLALchemy object
class history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rarity = db.Column(db.String(60),nullable=False)
    gun = db.Column(db.String(60),nullable=False)

db.create_all()


@app.route('/')
def index():
    rarity = requests.get('http://rarity:5001/get/rarity').text
    gun = requests.get('http://gun:5002/get/gun').text

    payload = {'rarity':rarity, 'gun':gun}
    price = requests.get('http://price:5003/post/winnings', json=payload).json()

    rollhistory = history.query.order_by(desc(history.id)).limit(5).all()

    storeroll = history(rarity=rarity, gun=gun)
    db.session.add(storeroll)
    db.session.commit()

    date = datetime(datetime.now().year, datetime.now().month,datetime.now().day)

    return render_template("main.html",storeroll = storeroll, rollhistory = rollhistory, date=date, price=price)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)