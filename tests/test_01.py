import unittest
from app import app

class JsonPayloadTest(unittest.TestCase):
    def test_non_json_payload_rejected(self):
        with app.test_client() as client:
            response = client.post('/submit', data='bad', content_type='text/plain')
            self.assertEqual(response.status_code, 400)
            self.assertFalse(response.get_json()['success'])

if __name__ == '__main__': unittest.main()
