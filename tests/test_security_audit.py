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

    def test_reject_json_null(self):
        with app.test_client() as client:
            response = client.post('/submit', data="null", content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_reject_json_boolean(self):
        with app.test_client() as client:
            response = client.post('/submit', data="true", content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_empty(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = ''
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)
