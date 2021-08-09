from flask import Flask, jsonify
import random
app = Flask(__name__)

@app.route("/get/gun", methods =["GET","POST"])
def gun():
    gun = open("gun.txt","r")
    gunlist = gun.readlines()
    return jsonify(random.choice(gunlist).strip())


if __name__=='__main__': app.run(host = "0.0.0.0", port=5003, debug=True)