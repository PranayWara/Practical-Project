from flask import Flask, redirect, render_template, request,url_for 
import random
app = Flask(__name__)

@app.route("/get/gun", methods =["GET","POST"])
def gun():
    gun = open("rarity.txt","r")
    gunlist = gun.readlines()
    return random.choice(gunlist)


if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)