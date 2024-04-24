import mysql.connector
from db_connector import connect_to_database, close_connection
from flask import Flask, request, jsonify


db_connection = connect_to_database()
cursor = db_connection.cursor()
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
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
        return jsonify({'message': 'Produit non trouvé'}), 404
    
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    query = "UPDATE customers SET FirstName = %s, LastName = %s, Email = %s WHERE CustomerID = %s"
    values = (data['FirstName'], data['LastName'], data['Email'], customer_id)
    cursor.execute(query, values)
    db_connection.commit()
    return jsonify({'message': 'Fiche client mise à jour avec succès!'})    

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    query = "INSERT INTO produits (Nom, Description, PrixUnitaire, Stock, Fournisseur) VALUES (%s, %s, %s, %s, %s)"
    values = (data['Nom'], data['Description'], data['PrixUnitaire'], data['Stock'], data['Fournisseur'])
    cursor.execute(query, values)
    db_connection.commit()
    return jsonify({'message': 'Product added successfully!'})

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    cursor.execute("DELETE FROM customers WHERE CustomerID = %s", (customer_id,))
    db_connection.commit()
    return jsonify({'message': 'Fiche client supprimée avec succès!'})

if __name__ == '__main__':
    app.run(debug=True)