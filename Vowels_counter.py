def count_vowel_words(sentence):
    count = 0
    words = sentence.lower().split()
    vowels = 'aeiou'
    for word in words:
        if word[0] in vowels:
            count += 1
    return count
