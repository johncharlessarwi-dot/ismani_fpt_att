import unittest
from app import app

class AdminCacheTest(unittest.TestCase):
    def test_unauthorized_admin_does_not_expose_data(self):
        with app.test_client() as client:
            r=client.get('/admin')
            self.assertEqual(r.status_code,401)
            self.assertNotIn(b'Attendance Dashboard',r.data)

if __name__=='__main__': unittest.main()
