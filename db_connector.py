import mysql.connector

def connect_to_database():
    host = "localhost"
    port = 3306
    user = "root"
    database = "mspr2"

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            database=database
        )

        if connection.is_connected():
            print("Connexion à la base de données réussie.")
            return connection

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

    return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée.")