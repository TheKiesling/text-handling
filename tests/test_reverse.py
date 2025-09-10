import unittest
from text_handling.text_handling import TextHandling


class TestReverse(unittest.TestCase):
    def test_reverse_basic_word(self):
        self.assertEqual(TextHandling.reverse("hola"), "aloh")

    def test_reverse_with_spaces_and_punct(self):
        self.assertEqual(TextHandling.reverse("Hola, mundo!"), "!odnum ,aloH")

    def test_reverse_empty_string(self):
        self.assertEqual(TextHandling.reverse(""), "")

    def test_reverse_failure(self):
        self.assertNotEqual(TextHandling.reverse("test"), "test")


if __name__ == "__main__":
    unittest.main()