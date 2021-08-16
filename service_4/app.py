from flask import Flask, request, jsonify



app = Flask(__name__)

sp = {
    'rarity':{
        'Hat': 1,
        'T-shirt': 1,
        'Jumper': 5,
        'Shorts': 20
    },
    'gun':{
        'Jordan': 5,
        'Nike': 3,
        'Adidas': 4,
        'Puma': 1,
    }
}

@app.route('/post/winnings', methods=['POST','GET'])

def price():

    rarity = request.get_json()["rarity"]
    gun = request.get_json()["gun"]
    price = sp['rarity'][rarity] + sp['gun'][gun]

    return jsonify(price)
    
if __name__=='__main__': app.run(host = "0.0.0.0", port=5004, debug=True)