import unittest
from text_handling.text_handling import TextHandling


class TestConcat(unittest.TestCase):
    def test_concat_basic_words(self):
        self.assertEqual(TextHandling.concat("hola", "mundo"), "holamundo")

    def test_concat_with_spaces_and_punct(self):
        self.assertEqual(TextHandling.concat("Hola, ", "mundo!"), "Hola, mundo!")

    def test_concat_empty_string(self):
        self.assertEqual(TextHandling.concat("", "mundo"), "mundo")
        self.assertEqual(TextHandling.concat("hola", ""), "hola")

    def test_concat_array_input(self):
        with self.assertRaises(TypeError):
            TextHandling.concat(['a', 'b'], 'c')
        with self.assertRaises(TypeError):
            TextHandling.concat('a', ['b', 'c'])