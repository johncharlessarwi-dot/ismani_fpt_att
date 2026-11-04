import unittest
from app import app, get_ip

class ClientIpTest(unittest.TestCase):
    def test_spoofed_forward_header_ignored(self):
        with app.test_request_context('/', environ_base={'REMOTE_ADDR':'127.0.0.2'}, headers={'X-Forwarded-For':'8.8.8.8'}):
            self.assertEqual(get_ip(), '127.0.0.2')

if __name__ == '__main__': unittest.main()
