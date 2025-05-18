def capitalize_words(sentence):
    capitalized = ''
    words = sentence.split()
    for word in words:
        capitalized += word[0].upper()
        capitalized += word[1:] + ' '
    return capitalize
