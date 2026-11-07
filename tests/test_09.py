import os
import unittest
from unittest.mock import patch
from app import app

class AdminAuthenticationTest(unittest.TestCase):
    def test_url_token_never_authorizes(self):
        with patch.dict(os.environ, {'ADMIN_TOKEN':'a'*32}):
            with app.test_client() as client:
                self.assertEqual(client.get('/admin?token=' + 'a'*32).status_code,401)
    def test_short_configured_token_rejected(self):
        with patch.dict(os.environ, {'ADMIN_TOKEN':'weak'}):
            with app.test_client() as client:
                self.assertEqual(client.get('/admin', headers={'X-Admin-Token':'weak'}).status_code,401)
    def test_oversized_token_is_rejected(self):
        with patch.dict(os.environ, {'ADMIN_TOKEN': 'a'*32}):
            with app.test_client() as client:
                self.assertEqual(client.get('/admin', headers={'X-Admin-Token':'a'*300}).status_code, 401)

    def test_missing_header_rejected_with_strong_secret(self):
        with patch.dict(os.environ, {'ADMIN_TOKEN':'a'*32}):
            with app.test_client() as client:
                self.assertEqual(client.get('/admin').status_code,401)
if __name__ == '__main__': unittest.main()
