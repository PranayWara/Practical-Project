from flask import Flask
import random

app = Flask(__name__)

def Rarity():
    i = random.randint(0,100)
    if i >= 0 and i < 80:
        return ('Blue') 
    elif i >= 80 and i < 95:
        return ('Purple') 
    elif i >= 95 and i < 99:
        return ('Pink') 
    else:
        return ('Red') 

if __name__ == '__main__':
    app.run(host='0.0.0.0')