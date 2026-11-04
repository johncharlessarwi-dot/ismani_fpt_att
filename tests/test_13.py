import unittest
from app import app

class SecurityHeadersTest(unittest.TestCase):
    def test_frame_and_mime_protection(self):
        with app.test_client() as client:
            r=client.get('/')
            self.assertEqual(r.headers['X-Frame-Options'],'DENY')
            self.assertEqual(r.headers['X-Content-Type-Options'],'nosniff')

if __name__=='__main__': unittest.main()
