import unittest
from app import app

class SecurityHeadersTest(unittest.TestCase):
    def test_frame_and_mime_protection(self):
        with app.test_client() as client:
            r=client.get('/')
            self.assertEqual(r.headers['X-Frame-Options'],'DENY')
            self.assertEqual(r.headers['X-Content-Type-Options'],'nosniff')

    def test_referrer_policy(self):
        with app.test_client() as client:
            self.assertEqual(client.get('/').headers.get('Referrer-Policy'), 'no-referrer')
    def test_legacy_cross_domain_disabled(self):
        with app.test_client() as client:
            self.assertEqual(client.get('/').headers.get('X-Permitted-Cross-Domain-Policies'), 'none')
if __name__=='__main__': unittest.main()
