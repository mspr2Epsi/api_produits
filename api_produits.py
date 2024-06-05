from flask import Flask, request, jsonify
from db_connector import connect_to_database
from roles import read_possible, update_possible, creation_possible, delete_possible
import pika
from datetime import datetime

def create_app():
    app = Flask(__name__)
    rabbitmq_host = 'rabbitmq'
    rabbitmq_port = 5672
    rabbitmq_user = 'user'
    rabbitmq_password = 'password'

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=rabbitmq_host,
                port=rabbitmq_port,
                credentials=credentials
            )
    )
    channel = connection.channel()
    channel.queue_declare(queue='message_broker_client')


    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    @app.route('/products', methods=['GET'])
    def get_products():
        begin_time = datetime.now()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  get_products")        
        token = request.headers.get('Authorization')
        if not read_possible(token):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement get_products termine")    
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
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 200 traitement get_products termine")      
        return jsonify({'products': output})

    @app.route('/products/<int:produit_id>', methods=['GET'])
    def get_product(produit_id):
        begin_time = datetime.now()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  get_products by ID")            
        token = request.headers.get('Authorization')
        if not read_possible(token):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement get_products by ID termine")              
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
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 404 traitement get_products by ID termine")              
            return jsonify({'message': 'Product not found'}), 404

    @app.route('/products', methods=['POST'])
    def add_product():
        begin_time = datetime.now()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  add_product")   
        token = request.headers.get('Authorization')
        if not creation_possible(token):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement add_product termine")                
            return jsonify({'message': 'Unauthorized'}), 401
           
        data = request.get_json()
        query = "INSERT INTO produits (Nom, Description, PrixUnitaire, Stock, Fournisseur) VALUES (%s, %s, %s, %s, %s)"
        values = (data['Nom'], data['Description'], data['PrixUnitaire'], data['Stock'], data['Fournisseur'])
        cursor.execute(query, values)
        db_connection.commit()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 201 traitement add_product termine")           
        return jsonify({'message': 'Product added successfully!'}), 201

    @app.route('/products/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        begin_time = datetime.now()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  delete_product")           
        token = request.headers.get('Authorization')
        if not delete_possible(token):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement delete_product termine")              
            return jsonify({'message': 'Unauthorized'}), 401 
            
        cursor.execute("DELETE FROM produits WHERE ProduitID = %s", (product_id,))
        db_connection.commit()  
        if cursor.rowcount > 0:
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 200 traitement delete_product termine")              
            return jsonify({'message': 'Product deleted successfully'}), 200
        else:
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 404 traitement delete_product termine")              
            return jsonify({'message': 'Product not found'}), 404

    @app.route('/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        begin_time = datetime.now()
        channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  update_product")             
        token = request.headers.get('Authorization')
        if not update_possible(token):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement update_product termine")               
            return jsonify({'message': 'Unauthorized'}), 401 
        
        data = request.get_json()  
        required_keys = ['Nom', 'Description', 'PrixUnitaire', 'Stock', 'Fournisseur']
        if not all(key in data for key in required_keys):
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 400 traitement update_product termine")               
            return jsonify({'message': 'Incomplete data'}), 400

        cursor.execute("""
            UPDATE produits 
            SET Nom = %s, Description = %s, PrixUnitaire = %s, Stock = %s, Fournisseur = %s 
            WHERE ProduitID = %s
            """, (data['Nom'], data['Description'], data['PrixUnitaire'], data['Stock'], data['Fournisseur'], product_id))
        db_connection.commit()  

        if cursor.rowcount > 0:
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 200 traitement update_product termine")               
            return jsonify({'message': 'Product updated successfully'}), 200
        else:
            channel.basic_publish(exchange='', routing_key='message_broker_produit', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 404 traitement update_product termine")               
            return jsonify({'message': 'Product not found'}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000,debug=True)

