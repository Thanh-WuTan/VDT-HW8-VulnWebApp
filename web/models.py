from . import db
 
class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


