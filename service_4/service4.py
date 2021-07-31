from service_2.service2 import Rarity
from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'Rarity':{
        'Blue': 0.30,
        'Purple': 1.00,
        'Pink': 5.00,
        'Red': 20.00
    },
    'Gun':{
        'AK-47': 5.00,
        'M4A4': 3.00,
        'AWP': 4.00,
        'Glock-18': 1.00,
        'USP-S': 2.00,
    }
}

@app.route('/post/order', methods=['POST'])

def price():
    Rarity = request.json['Rarity']
    Guns = request.json['Guns']

    price = prices['Rarity'][Rarity] + prices['Guns'][Guns]
    
    return jsonify(price)