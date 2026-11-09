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

    def test_reject_reg_one_character(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'A'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_spaces(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = '   '
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_embedded_space(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'ABC 123'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_leading_punctuation(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = '-ABC'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_at_sign(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'ABC@123'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_unicode(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'ÅBC123'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_newline(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'ABC\n123'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_tab(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'ABC\t123'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_overlength(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 'A' * 51
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_numeric(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = 123
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_reg_missing(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['reg_number'] = None
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_name_empty(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['full_name'] = ''
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_name_spaces(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['full_name'] = '   '
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_name_newline(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['full_name'] = 'John\nDoe'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_name_tab(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['full_name'] = 'John\tDoe'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)

    def test_reject_name_del(self):
        with app.test_client() as client:
            data = { 'reg_number': 'T/DEG/2025/0817', 'full_name': 'Test Student', 'company': 'Ismani Tours and Safari' }
            data['full_name'] = 'John\x7fDoe'
            response = client.post('/submit', json=data, headers={'User-Agent':'AuditClient/1.0'})
            self.assertEqual(response.status_code, 400)
