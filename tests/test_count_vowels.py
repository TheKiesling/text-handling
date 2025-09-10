import unittest
from text_handling.text_handling import TextHandling


class TestCountVowels(unittest.TestCase):
    def test_count_vowels_basic_word(self):
        self.assertEqual(TextHandling.count_vowels("hola"), 2)

    def test_count_vowels_with_spaces_and_punct(self):
        self.assertEqual(TextHandling.count_vowels("Hola, mundo!"), 4)

    def test_count_vowels_array_input(self):
        with self.assertRaises(TypeError):
            TextHandling.count_vowels(['a', 'b'])
            
    def test_count_vowels_with_dummy_vowels(self):
        phishing_word = "раpеr"
        self.assertEqual(TextHandling.count_vowels(phishing_word), 0)
