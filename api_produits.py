from db_connector import connect_to_database, close_connection
from flask import Flask, request, jsonify
from roles import  read_possible,update_possible,creation_possible,delete_possible

db_connection = connect_to_database()
cursor = db_connection.cursor()
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401
    
    cursor.execute("SELECT * FROM produits")
    products = cursor.fetchall()
    output = []
    for product in products:
        product_data = {
            'ProduitID': product[0],
            'Nom': product[1],
            'Description': product[2],
            'PrixUnitaire': float(product[3]),
            'Stock': product[4],
            'Fournisseur': product[5]
        }
        output.append(product_data)
    return jsonify({'products': output})

@app.route('/products/<int:produit_id>', methods=['GET'])
def get_product(produit_id):
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401
    
    cursor.execute("SELECT * FROM produits WHERE ProduitID = %s", (produit_id,))
    product = cursor.fetchone()
    if product:
        product_data = {
            'ProduitID': product[0],
            'Nom': product[1],
            'Description': product[2],
            'PrixUnitaire': float(product[3]),
            'Stock': product[4],
            'Fournisseur': product[5]
        }
        return jsonify(product_data)
    else:
        return jsonify({'message': 'Product not found'}), 404
    
@app.route('/products', methods=['POST'])
def add_product():
    token = request.headers.get('Authorization')
    if creation_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401 
       
    data = request.get_json()
    query = "INSERT INTO produits (Nom, Description, PrixUnitaire, Stock, Fournisseur) VALUES (%s, %s, %s, %s, %s)"
    values = (data['Nom'], data['Description'], data['PrixUnitaire'], data['Stock'], data['Fournisseur'])
    cursor.execute(query, values)
    db_connection.commit()
    return jsonify({'message': 'Product added successfully!'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    token = request.headers.get('Authorization')
    if delete_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401 
        
    cursor.execute("DELETE FROM produits WHERE ProduitID = %s", (product_id,))
    db_connection.commit()  
    if cursor.rowcount > 0:
        return jsonify({'message': 'Product deleted with success'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    token = request.headers.get('Authorization')
    if update_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401 
    
    data = request.get_json()  
    required_keys = ['Nom', 'Description', 'PrixUnitaire', 'Stock', 'Fournisseur']
    if not all(key in data for key in required_keys):
        return jsonify({'message': 'Incomplete data'}), 400

    cursor.execute("""
        UPDATE produits 
        SET Nom = %s, Description = %s, PrixUnitaire = %s, Stock = %s, Fournisseur = %s 
        WHERE ProduitID = %s
        """, (data['Nom'], data['Description'], data['PrixUnitaire'], data['Stock'], data['Fournisseur'], product_id))
    db_connection.commit()  

    if cursor.rowcount > 0:
        return jsonify({'message': 'product updated with sucess'}), 200
    else:
        return jsonify({'message': 'product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)