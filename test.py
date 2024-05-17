import unittest
from flask import url_for
from flask_testing import TestCase
from api_produits import create_app
from db_connector import connect_to_database, close_connection

class TestFlaskApp(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/mspr2'
        return app

    def setUp(self):
        self.db_connection = connect_to_database()
        self.cursor = self.db_connection.cursor()
        # Set up test data (if needed) in the database
        # Example: self.cursor.execute("CREATE TABLE ...")

    def tearDown(self):
        # Clean up after each test
        # Example: self.cursor.execute("DROP TABLE ...")
        self.db_connection.close()  # Close the database connection

    # Tests unitaires
    def tests_unitaires(self):
        self.test_get_product()
        self.test_get_product_not_found()
        self.test_add_product()
        self.test_delete_product()
        self.test_delete_nonexistent_product()
        self.test_update_product()
        self.test_update_nonexistent_product()

    # Tests d'intégration
    def test_integration(self):
        self.test_get_products()
        self.test_add_product()
        self.test_update_product()
        self.test_delete_product()

    # Tests fonctionnels
    def test_fonctionnel(self):
        self.test_get_products()
        self.test_add_product()
        self.test_update_product()
        self.test_delete_product()

    # Tests de régression
    def test_regression(self):
        self.test_get_product()
        self.test_get_product_not_found()
        self.test_update_nonexistent_product()

    # Tests de performance
    def test_performance(self):
        # Placeholder
        pass

    # Tests de sécurité
    def test_securite(self):
        # Placeholder
        pass


    def test_get_products(self):
        response = self.client.get('/products', headers={'Authorization': 'omzRfFaKaZsI1LkziC8co7dMEb9cKgzBvJbOfrHkv0KDcXQGfMZj1iFHeLRmoXPD'})
        self.assert200(response)
        self.assertIn(b'products', response.data)

    def test_get_product(self):
        response = self.client.get('/products/1', headers={'Authorization': 'omzRfFaKaZsI1LkziC8co7dMEb9cKgzBvJbOfrHkv0KDcXQGfMZj1iFHeLRmoXPD'})
        self.assert200(response)
        self.assertIn(b'ProduitID', response.data)

    def test_get_product_not_found(self):
        response = self.client.get('/products/999', headers={'Authorization': 'omzRfFaKaZsI1LkziC8co7dMEb9cKgzBvJbOfrHkv0KDcXQGfMZj1iFHeLRmoXPD'})
        self.assert404(response)
        self.assertIn(b'Product not found', response.data)

    def test_add_product(self):
        data = {
            'Nom': 'New Product',
            'Description': 'A new product',
            'PrixUnitaire': 10.99,
            'Stock': 100,
            'Fournisseur': 'Supplier X'
        }
        response = self.client.post('/products', json=data, headers={'Authorization': 'vyS2L3ieJBe4hI5k5CQZ1JGY3OqUl7G8suTvtJAxvuYDaX85y0d9e9UzW7wQsUeE'})
        self.assertStatus(response, 201)
        self.assertIn(b'Product added successfully', response.data)

    def test_delete_product(self):
        response = self.client.delete('/products/1', headers={'Authorization': 'keFcYRLjAS4Tq6hEp4JFPkGR1d0IHJd58Xe2mvkz2gidmRg4v5B0QWhbAVlJ4Kts'})
        self.assert200(response)
        self.assertIn(b'Product deleted successfully', response.data)

    def test_delete_nonexistent_product(self):
        response = self.client.delete('/products/999', headers={'Authorization': 'keFcYRLjAS4Tq6hEp4JFPkGR1d0IHJd58Xe2mvkz2gidmRg4v5B0QWhbAVlJ4Kts'})
        self.assert404(response)
        self.assertIn(b'Product not found', response.data)

    def test_update_product(self):
        data = {
            'Nom': 'Updated Product Name',
            'Description': 'Updated description',
            'PrixUnitaire': 15.99,
            'Stock': 200,
            'Fournisseur': 'Supplier Y'
        }
        response = self.client.put('/products/1', json=data, headers={'Authorization': 'A6s4kRxuawKMrXzKe9Y6drksvDXLAcOc6GISk7v8RDlPM8VLxqYSBAQrWfQkzm44'})
        self.assert200(response)
        self.assertIn(b'Product updated successfully', response.data)

    def test_update_nonexistent_product(self):
        data = {
            'Nom': 'Updated Product Name',
            'Description': 'Updated description',
            'PrixUnitaire': 15.99,
            'Stock': 200,
            'Fournisseur': 'Supplier Y'
        }
        response = self.client.put('/products/999', json=data, headers={'Authorization': 'A6s4kRxuawKMrXzKe9Y6drksvDXLAcOc6GISk7v8RDlPM8VLxqYSBAQrWfQkzm44'})
        self.assert404(response)
        self.assertIn(b'Product not found', response.data)


# if __name__ == '__main__':
#     choix = int(input("""Liste des tests :
#                   1. Tests unitaires
#                   2. Tests d'intégration
#                   3. Tests fonctionnels
#                   4. Tests de régression
#                   Quel est votre choix ?
#                   """))

#     choice_ok = [1, 2, 3, 4]
#     while choix not in choice_ok:
#         choix = int(input("Veuillez renseigner un choix valide (1, 2, 3, 4)\n"))

#     suite = unittest.TestSuite()
#     test_loader = unittest.TestLoader()

#     if choix == 1:
#         suite.addTests(test_loader.loadTestsFromName('TestFlaskApp.tests_unitaires'))
#     elif choix == 2:
#         suite.addTests(test_loader.loadTestsFromName('TestFlaskApp.test_integration'))
#     elif choix == 3:
#         suite.addTests(test_loader.loadTestsFromName('TestFlaskApp.test_fonctionnel'))
#     elif choix == 4:
#         suite.addTests(test_loader.loadTestsFromName('TestFlaskApp.test_regression'))

#     runner = unittest.TextTestRunner()
#     runner.run(suite)