from flask import render_template
from sqlalchemy import desc
import requests
from application.models import history
from application import app, db

@app.route('/', methods = ['POST','GET'])
def index():
    rarity = requests.get('http://service_2:5002/get/rarity').json()
    gun = requests.get('http://service_3:5003/get/gun').json()

    price = requests.post('http://service_4:5004/post/winnings', json={"rarity":rarity, "gun":gun}).json()
 
    rollhistory = history.query.order_by(desc(history.id)).limit(5).all()

    storeroll = history(rarity=rarity, gun=gun, price=price)
    db.session.add(storeroll)
    db.session.commit()

    

    return render_template("main.html",storeroll = storeroll, rollhistory = rollhistory)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)