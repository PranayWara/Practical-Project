from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# @app.route('/post/winnings', methods=['POST'])

# def price():
    # rarity_price = requests.get('http://service_2:5001/get/rarity').text
    # guns_price = requests.get('http://sercive_3:5002/get/gun').text
    # if rarity_price == 'Blue':
    #     rp = 1
    # elif rarity_price == 'Purple':
    #     rp = 2
    # elif rarity_price == 'Pink':
    #     rp = 5
    # elif rarity_price == 'Red':
    #     rp = 20
    # elif guns_price == 'AK-47':
    #     gp = 5
    # elif guns_price == 'M4A4':
    #     gp = 3
    # elif guns_price == 'AWP':
    #     gp = 4
    # elif guns_price == 'Glock-18':
    #     gp = 1
    # elif guns_price == 'USP-S':
    #     gp = 2
    # price = rp + gp
    # return jsonify(price)

prices = {
    'rarity':{
        'Blue': 0.30,
        'Purple': 1.00,
        'Pink': 5.00,
        'Red': 20.00
    },
    'gun':{
        'AK-47': 5.00,
        'M4A4': 3.00,
        'AWP': 4.00,
        'Glock-18': 1.00,
        'USP-S': 2.00,
    }
}

@app.route('/post/winnings', methods=['POST'])

def post_winnings():
    rarity = request.json['Rarity']
    guns = request.json['Guns']

    price = prices['rarity'][rarity] + prices['guns'][guns]
    return jsonify(price)

if __name__=='__main__': app.run(host = "0.0.0.0", port=5004, debug=True)