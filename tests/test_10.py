import os
import unittest
from unittest.mock import patch
from app import app

class AdminHeaderAcceptanceTest(unittest.TestCase):
    def test_admin_accepts_valid_header(self):
        with patch.dict(os.environ, {'ADMIN_TOKEN': 'a' * 32}):
            with app.test_client() as client:
                response = client.get('/admin', headers={'X-Admin-Token': 'a' * 32})
                self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
