import unittest
from text_handling.text_handling import TextHandling


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_basic(self):
        self.assertEqual(TextHandling.is_palindrome("ana"), True)
        
    def test_is_palindrome_with_spaces_and_punct(self):
        self.assertEqual(TextHandling.is_palindrome("A man, a plan, a canal: Panama"), True)
        
    def test_is_palindrome_not_palindrome(self):
        self.assertEqual(TextHandling.is_palindrome("hello"), False)
        
    def test_is_palindrome_array_input(self):
        with self.assertRaises(TypeError):
            TextHandling.is_palindrome(['a', 'b'])
            
    def test_is_palindrome_with_dummy_word(self):
        phishing_word = "a|omola"
        self.assertEqual(TextHandling.is_palindrome(phishing_word), False)