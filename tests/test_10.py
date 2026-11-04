import unittest
from unittest.mock import patch
from app import app

class AdminHeaderAcceptanceTest(unittest.TestCase):
    def test_admin_accepts_valid_header(self):
        with patch('app.os.getenv', side_effect=lambda key, default=None: 'a'*32 if key == 'ADMIN_TOKEN' else default):
            with patch('app.Attendance.query') as query:
                query.filter_by.return_value.order_by.return_value.all.return_value = []
                query.order_by.return_value.limit.return_value.all.return_value = []
                with app.test_client() as client:
                    response = client.get('/admin', headers={'X-Admin-Token':'a'*32})
                    self.assertEqual(response.status_code, 200)

if __name__ == '__main__': unittest.main()
