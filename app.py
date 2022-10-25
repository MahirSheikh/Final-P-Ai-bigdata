from flask import Flask, jsonify, request
products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]
app = Flask(__name__)
# curl -v http://localhost:8080/products
@app.route('/products')
def get_products():
    return jsonify(products)

# curl -v http://localhost:8080/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] ==id]
    if len(product_list) == 0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0]) 


# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:8080/product
@app.route('/product', methods=['POST'])
def post_product():
    # Retrieve the product from the request body
    request_product = request.json
    # Generate an ID for the post
    new_id = max([product['id'] for product in products]) + 1
    # Create a new product
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }
    # Append the new product to our product list
    products.append(new_product)
    # Return the new product back to the client
    return jsonify(new_product), 201

# curl -- header "Content-Type: application/json" --request PUT --data'{"name": "Updated Product 2"}' -v http://localhost:8080/product/2
@app.route('/product/<int:id>', methods=['PUT'])
    # Get the request payload
def put_product():

    updated_product = request.json
    # Find the product with the specified ID
    for product in products:
        if product['id'] == id:
            # Update the product name
            product['name'] = updated_product['name']
            return jsonify(product), 200
    return f'Product with id {id} not found', 404

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Find the product with the specified ID
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'Product with id {id} deleted', 200
    return f'Product with id {id} not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
# will use port 500 accessible from external to our computer if not it will use localhost
