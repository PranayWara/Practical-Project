from flask import Flask, request, jsonify

app = Flask(__name__)

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

def price():
    rarity = request.json['Rarity']
    guns = request.json['Guns']

    price = prices['rarity'][rarity] + prices['guns'][guns]
    
    return jsonify(price)

if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)