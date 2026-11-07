import unittest
from app import safe_metadata

class MetadataTest(unittest.TestCase):
    def test_non_text_removed(self):
        self.assertEqual(safe_metadata({'nested':'data'}), '')
    def test_oversized_text_trimmed(self):
        self.assertEqual(safe_metadata('abcdef', 3), 'abc')
    def test_strips_control_characters(self):
        self.assertEqual(safe_metadata('abc\n\tdef'), 'abcdef')

if __name__ == '__main__': unittest.main()
