from flask import Flask
import random

app = Flask(__name__)


gun = ['AK-47', 'M4A4', 'AWP', 'Glock-18', 'USP-S']

def Gun():
    return random.choice(gun)

if __name__ == '__main__':
    app.run(host='0.0.0.0')