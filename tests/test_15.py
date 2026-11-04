import unittest
from app import app

class NotificationFallbackTest(unittest.TestCase):
    def test_validation_does_not_require_mail_credentials(self):
        with app.test_client() as client:
            r=client.post('/submit',json={'reg_number':'','full_name':'Student','company':'Ismani Tours and Safari'})
            self.assertEqual(r.status_code,400)

if __name__=='__main__': unittest.main()
