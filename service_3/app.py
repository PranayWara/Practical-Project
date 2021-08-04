from flask import Flask
import random
app = Flask(__name__)

@app.route("/get/gun", methods =["GET","POST"])
def gun():
    gun = open("gun.txt","r")
    gunlist = gun.readlines()
    return random.choice(gunlist)


if __name__=='__main__': app.run(host = "0.0.0.0")