import unittest

from app import safe_coordinate


class CoordinateValidationTests(unittest.TestCase):
    def test_accepts_valid_latitude_and_longitude(self):
        self.assertEqual(safe_coordinate('-3.33', 90), '-3.33')
        self.assertEqual(safe_coordinate(180, 180), '180.0')
        self.assertEqual(safe_coordinate('-90', 90), '-90.0')

    def test_rejects_nonfinite_values(self):
        for value in ('NaN', 'Infinity', '-Infinity', float('nan'), float('inf')):
            with self.subTest(value=str(value)):
                self.assertEqual(safe_coordinate(value, 90), '')

    def test_rejects_out_of_bounds_and_invalid_values(self):
        for value in ('91', '-91', 'abc', [], None):
            with self.subTest(value=value):
                self.assertEqual(safe_coordinate(value, 90), '')

    def test_reject_boolean_latitude(self):
        self.assertEqual(safe_coordinate(True, 90), '')

if __name__ == '__main__':
    unittest.main()
