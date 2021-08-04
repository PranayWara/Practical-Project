from flask import Flask 
import random
app = Flask(__name__)

@app.route("/get/rarity", methods =["GET","POST"])
def rarity():
    rarity = open("rarity.txt","r")
    raritylist = rarity.readlines()
    return random.choice(raritylist)


if __name__=='__main__': app.run(host = "0.0.0.0")