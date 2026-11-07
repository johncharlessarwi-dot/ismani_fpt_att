import unittest
from app import safe_metadata

class MetadataTest(unittest.TestCase):
    def test_non_text_removed(self):
        self.assertEqual(safe_metadata({'nested':'data'}), '')
    def test_oversized_text_trimmed(self):
        self.assertEqual(safe_metadata('abcdef', 3), 'abc')
    def test_strips_control_characters(self):
        self.assertEqual(safe_metadata('abc\n\tdef'), 'abcdef')
    def test_limit_is_clamped(self):
        self.assertEqual(len(safe_metadata('x'*1000, 1000)), 512)
    def test_invalid_limit_falls_back(self):
        self.assertEqual(len(safe_metadata('x'*150, 'invalid')), 100)
    def test_zero_limit_is_empty(self):
        self.assertEqual(safe_metadata('xyz', 0), '')

    def test_list_metadata_is_ignored(self):
        self.assertEqual(safe_metadata(['Chrome']), '')
    def test_normal_language_tag(self):
        self.assertEqual(safe_metadata('sw-TZ', 20), 'sw-TZ')
if __name__ == '__main__': unittest.main()
