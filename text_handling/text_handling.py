class TextHandling(Exception):
    def reverse(s):
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        return s[::-1]
    
    def count_vowels(s):
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)
    
    def is_palindrome(s):
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]
