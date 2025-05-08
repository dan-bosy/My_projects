import string

def count_vowels_consonants(s):
    letters = string.ascii_lowercase
    vowels = 'aeiou'
    consonants = [char for char in letters if char not in vowels]
    
    vowel_count, consonant_count = 0, 0
    for char in s.lower():
        if char in letters:
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_coun
