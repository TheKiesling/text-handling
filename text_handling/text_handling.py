class TextHandling(Exception):
    def reverse(s):
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        return s[::-1]
