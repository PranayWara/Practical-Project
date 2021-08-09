from flask import Flask, request, jsonify



app = Flask(__name__)

sp = {
    'rarity':{
        'Blue': 1,
        'Purple': 1,
        'Pink': 5,
        'Red': 20
    },
    'gun':{
        'AK-47': 5,
        'M4A4': 3,
        'AWP': 4,
        'Glock-18': 1,
        'USP-S': 2,
    }
}

@app.route('/post/winnings', methods=['POST','GET'])

def price():

    rarity = request.get_json()["rarity"]
    gun = request.get_json()["gun"]
    price = sp['rarity'][rarity] + sp['gun'][gun]

    return jsonify(price)
    
if __name__=='__main__': app.run(host = "0.0.0.0", port=5004, debug=True)