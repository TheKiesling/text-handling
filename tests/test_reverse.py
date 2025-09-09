import unittest
from text_handling.reverse import reverse


class TestReverse(unittest.TestCase):
    def test_reverse_basic_word(self):
        self.assertEqual(reverse("hola"), "aloh")

    def test_reverse_with_spaces_and_punct(self):
        self.assertEqual(reverse("Hola, mundo!"), "!odnum ,aloH")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse(""), "")

    def test_reverse_raises_typeerror_on_int(self):
        with self.assertRaises(TypeError):
            reverse(123)

    def test_reverse_raises_typeerror_on_list(self):
        with self.assertRaises(TypeError):
            reverse(['a', 'b'])


if __name__ == "__main__":
    unittest.main()