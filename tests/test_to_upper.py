import unittest
from text_handling.text_handling import TextHandling


class TestToUpper(unittest.TestCase):
    def test_to_upper_basic_word(self):
        self.assertEqual(TextHandling.to_upper("hola"), "HOLA")

    def test_to_upper_with_mixed_case(self):
        self.assertEqual(TextHandling.to_upper("Hola, Mundo!"), "HOLA, MUNDO!")

    def test_to_upper_empty_string(self):
        self.assertEqual(TextHandling.to_upper(""), "")

    def test_to_upper_array_input(self):
        with self.assertRaises(TypeError):
            TextHandling.to_upper(['a', 'b'])
    