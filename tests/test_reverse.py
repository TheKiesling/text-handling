import unittest
from text_handling.text_handling import TextHandling


class TestReverse(unittest.TestCase):
    def test_reverse_basic_word(self):
        self.assertEqual(TextHandling.reverse("hola"), "aloh")

    def test_reverse_with_spaces_and_punct(self):
        self.assertEqual(TextHandling.reverse("Hola, mundo!"), "!odnum ,aloH")
        
    def test_reverse_array_input(self):
        with self.assertRaises(TypeError):
            TextHandling.reverse(['a', 'b'])


if __name__ == "__main__":
    unittest.main()