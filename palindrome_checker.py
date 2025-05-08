import string

def is_palindrome(s):
    result = ''
    symbols = string.punctuation
    for c in s:
        if c not in symbols and c != ' ':
            result += c
    rev_result = result[::-1].lower()
    return rev_result == result.lower()
