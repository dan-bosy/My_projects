def remove_vowels(s):
    vowels = 'aeiou'
    no_vowels = ''
    for char in s.lower():
        if char not in vowels:
            no_vowels += char
    return no_vowels
