def count_words(s):
    words = s.lower()
    word_count = 0
    for word in words.split():
        word_count += 1
        
    return word_count
