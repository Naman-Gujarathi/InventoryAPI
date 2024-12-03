from flask import request, jsonify, Blueprint, abort
from model.product import Product
from db import db

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods = ['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200

# Get a single product by ID
@product_bp.route('/products/<int:product_id>', methods= ['GET'])
def get_product_by_id(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

#create a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    print("reacehd indie post body")
    data = request.get_json()
    if not data:
        return jsonify({'error' : 'No input data provided'}), 400
    name = data.get('name')
    price = float(data.get('price'))
    description = data.get('description')
    qty = int(data.get('qty', 0))

    new_product = Product(
        name=name, 
        description=description, 
        price=price, 
        qty=qty
    )
    print("going to commiting change")
    db.session.add(new_product)
    db.session.commit()
    print("commited")
    response = {"message" : "prodcut is successfuly added to databsae", 'product': new_product.to_dict()}, 201
    return jsonify(response)

# update an existing product

@product_bp.route('/products/<int:product_id>', methods = ['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    data = request.get_json()
    if not data:
        jsonify({'message': "bad request"}), 400
    
    product.name = data.get('name')
    product.price = float(data.get('price'))
    product.description = data.get('description')
    product.qty = int(data.get('qty'))

    db.session.commit()

    return jsonify({'message': 'product update', 'product': product.to_dict()}), 200

# delete an product
@product_bp.route('/products/<int:product_id>', methods = ['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200


