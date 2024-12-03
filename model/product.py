from db import db

class Product(db.Model):
    __tablename__ = 'product'  
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(300), nullable = True)
    price = db.Column(db.Float, nullable = False )
    qty = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return f"<Product {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'qty': self.qty
        }
