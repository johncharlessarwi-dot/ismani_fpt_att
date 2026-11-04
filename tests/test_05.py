import unittest
from app import app

class PlacementTest(unittest.TestCase):
    def test_arbitrary_company_rejected(self):
        with app.test_client() as client:
            response = client.post('/submit', json={'reg_number':'T123','full_name':'Student','company':'Unverified Vendor'})
            self.assertEqual(response.status_code,400)

if __name__ == '__main__': unittest.main()
