import unittest
from app import app

class RequestSizeTest(unittest.TestCase):
    def test_oversized_request_rejected(self):
        with app.test_client() as client:
            response=client.post('/submit',data='x'*17000,content_type='application/json')
            self.assertEqual(response.status_code,413)
    def test_submit_errors_are_not_cacheable(self):
        with app.test_client() as client:
            result = client.post('/submit', json={})
            self.assertIn('no-store', result.headers.get('Cache-Control',''))

if __name__=='__main__': unittest.main()
