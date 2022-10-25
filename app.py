from flask import Flask, jsonify, request
from parcinsson_Project_ready import *


app = Flask(__name__)
# curl -v http://localhost:8080/ui
@app.route('/ui', methods=['GET'])
def get_ui():
    ui=parcinsson_Project_ready.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #sys.exit(app.exec())
    return MainWindow.show()




import numpy as np
# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:8080/checksick
@app.route('/checksick', methods=['POST'])
def post_sick():
    
    # Retrieve the product from the request body
    request_data_sick = request.json # list with all the data
    # np.array([float(self.mdvpfo.toPlainText()), float(self.mdvpflo_hz.toPlainText()), float(self.mdvp_hitterpr.toPlainText()), float(self.jitterAbs.toPlainText()), float(self.mdvpRAP.toPlainText()), float(self.mdvpppq.toPlainText()),float(self.mdvpDDP.toPlainText()),float(self.mdvpSHIMMER.toPlainText()),float(self.mdvp_SHIMMERDB.toPlainText()), float(self.SHIMMERAPQ3.toPlainText()),float(self.SHIMMERAPq5.toPlainText()), float(self.MDVPAPQ.toPlainText()),float(self.SHIMMERDDA.toPlainText()),float(self.HNR.toPlainText()), float(self.RPDE.toPlainText()),float(self.DFA.toPlainText()),float(self.SPREAD1.toPlainText()),float(self.SPREAD2.toPlainText()),float(self.D2.toPlainText()),float(self.PPE.toPlainText())]).reshape(1, -1) # X is a matrix of features
    Ui_MainWindow()
    ui, sick = Ui_MainWindow()
    check_sick = request_data_sick.reshape(1, -1)

    if model.predict(check_sick)==[1]:
                print("yes")
                from PyQt6.QtWidgets import QMessageBox
                msg=QMessageBox()
                msg.setWindowTitle("resault")
                msg.setText("patient is sick")
                x=msg.exec()
                return jsonify({'message': 'patient is sick'})
    else:
                from PyQt6.QtWidgets import QMessageBox
                msg=QMessageBox()
                msg.setWindowTitle("resault")
                msg.setText("patient  isn't sick")
                x=msg.exec()
                return jsonify({'message': 'patient  isn"t sick'})
        
  

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
