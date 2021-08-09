from application import db


class history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rarity = db.Column(db.String(60),nullable=False)
    gun = db.Column(db.String(60),nullable=False)
    price = db.Column(db.Integer, primary_key=False)