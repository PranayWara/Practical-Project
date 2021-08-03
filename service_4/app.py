from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/post/winnings', methods=['POST'])

def price():
    rarity_price = requests.get('http://localhost:5001/get/rarity').text
    guns_price = requests.get('http://localhost:5002/get/gun').text
    if rarity_price == 'Blue':
        rp = 1
    elif rarity_price == 'Purple':
        rp = 2
    elif rarity_price == 'Pink':
        rp = 5
    elif rarity_price == 'Red':
        rp = 20
    elif guns_price == 'AK-47':
        gp = 5
    elif guns_price == 'M4A4':
        gp = 3
    elif guns_price == 'AWP':
        gp = 4
    elif guns_price == 'Glock-18':
        gp = 1
    elif guns_price == 'USP-S':
        gp = 2
    price = rp + gp
    return jsonify(price)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5003, debug=True)