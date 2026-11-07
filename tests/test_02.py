import unittest
from app import app

class LengthValidationTest(unittest.TestCase):
    def test_oversized_registration_rejected(self):
        with app.test_client() as client:
            response = client.post('/submit', json={'reg_number':'A'*51,'full_name':'Student','company':'Ismani Tours and Safari'})
            self.assertEqual(response.status_code,400)

    def test_extremely_long_registration_rejected(self):
        with app.test_client() as client:
            self.assertEqual(client.post('/submit', json={'reg_number':'X'*500,'full_name':'Student','company':'Ismani Tours and Safari'}).status_code,400)
if __name__ == '__main__': unittest.main()
