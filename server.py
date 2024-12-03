from flask import Flask, jsonify
import os
from db import db
from model.product import Product
from controller.product_controller import product_bp

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'test.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 

db.init_app(app)



with app.app_context():
    try:
        print('creating databas table')
        db.create_all()
        print("database table created")
    except Exception as e:
        print(f"an error occurr while creating db table: {e}")

app.register_blueprint(product_bp)

@app.route('/', methods=['GET'])
def function():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug = True) #by default flask runs on 5000 PORT number

