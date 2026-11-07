import unittest
from app import safe_coordinate

class CoordinatesTest(unittest.TestCase):
    def test_rejects_invalid_latitude(self):
        self.assertEqual(safe_coordinate('99',90),'')
        self.assertEqual(safe_coordinate('nan',90),'')
    def test_accepts_valid_longitude(self):
        self.assertEqual(safe_coordinate('36.8',180),'36.8')

    def test_rejects_nonnumber_longitude(self):
        self.assertEqual(safe_coordinate('invalid', 180), '')
    def test_rejects_overbound_longitude(self):
        self.assertEqual(safe_coordinate('181', 180), '')
if __name__ == '__main__': unittest.main()
