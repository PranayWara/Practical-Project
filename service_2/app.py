from flask import Flask, jsonify
import random


app = Flask(__name__)

@app.route("/get/rarity", methods =["GET","POST"])
def rarity():
    rarity = open("rarity.txt","r")
    raritylist = rarity.readlines()
    return jsonify(random.choice(raritylist).strip())


if __name__=='__main__': app.run(host = "0.0.0.0", port=5002, debug=True)