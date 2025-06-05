def capitalize_words(sentence):
    words = sentence.split()
    capitalized_word = ''
    for word in words:
        capitalized_word += word[0].upper()+word[1:]+ ' '
        
    return capitalized_word
