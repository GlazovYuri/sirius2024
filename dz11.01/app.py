#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

products = [
    {
        'id': 1,
        'title': 'Milk',
        'description': 'from cow'
    },
    {
        'id': 2,
        'title': 'Cookie',
        'description': 'from kitchen'
    }
]

@app.route('/list/api/v1.0/products', methods=['GET'])
def get_products():
    all_products = []
    for prod in products:
        all_products.append(prod['title'])
    return all_products

@app.route('/list/api/v1.0/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    if len(products) == 0 or len(products) < product_id or product_id <= 0:
        abort(404)
    return products[product_id-1]['title'] + ", " + products[product_id-1]['description']

@app.route('/list/api/v1.0/products', methods=['POST'])
def create_product():
    if not request.json or not 'title' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
    }
    products.append(product)
    return "Done"

@app.route('/list/api/v1.0/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if len(products) == 0:
        abort(404)
    if not request.json:
        abort(400)
    products[0]['title'] = request.json.get('title', products[0]['title'])
    products[0]['description'] = request.json.get('description', products[0]['description'])
    return "Done"

@app.route('/list/api/v1.0/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if len(products) == 0:
        abort(404)
    products.remove(products[0])
    return "Done"

if __name__ == '__main__':
    app.run(debug=True)
