import unittest
from app import app, safe_coordinate


class AttendanceSecurityAuditTests(unittest.TestCase):

    def test_reject_json_array(self):
        with app.test_client() as client:
            response = client.post('/submit', data="[]", content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_reject_json_string(self):
        with app.test_client() as client:
            response = client.post('/submit', data="\"hello\"", content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_reject_json_number(self):
        with app.test_client() as client:
            response = client.post('/submit', data="42", content_type='application/json')
            self.assertEqual(response.status_code, 400)
