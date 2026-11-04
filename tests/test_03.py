import unittest
from app import app

class TypedFieldsTest(unittest.TestCase):
    def test_non_string_name_rejected(self):
        with app.test_client() as client:
            response = client.post('/submit', json={'reg_number':'T123','full_name':42,'company':'Ismani Tours and Safari'})
            self.assertEqual(response.status_code,400)

if __name__ == '__main__': unittest.main()
