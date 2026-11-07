import unittest
from app import app

class ControlCharactersTest(unittest.TestCase):
    def test_newline_name_rejected(self):
        with app.test_client() as client:
            r=client.post('/submit',json={'reg_number':'T123','full_name':'Student\nName','company':'Ismani Tours and Safari'})
            self.assertEqual(r.status_code,400)

    def test_nul_name_rejected(self):
        with app.test_client() as client:
            self.assertEqual(client.post('/submit', json={'reg_number':'T123','full_name':'Student\u0000Name','company':'Ismani Tours and Safari'}).status_code,400)
    def test_tab_name_rejected(self):
        with app.test_client() as client:
            self.assertEqual(client.post('/submit', json={'reg_number':'T123','full_name':'Student\tName','company':'Ismani Tours and Safari'}).status_code,400)
if __name__=='__main__': unittest.main()
