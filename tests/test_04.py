import unittest
from app import app

class RegistrationFormatTest(unittest.TestCase):
    def test_control_characters_rejected(self):
        with app.test_client() as client:
            response = client.post('/submit', json={'reg_number':'T123\nX','full_name':'Student','company':'Ismani Tours and Safari'})
            self.assertEqual(response.status_code,400)

if __name__ == '__main__': unittest.main()
