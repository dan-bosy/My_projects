def longest_word(sentence):
    words = sentence.split()
    word_len = []
    longest = []
    for word in words:
        word_len.append(len(word))
        
    for text in words:
        if len(text) == max(word_len):
            longest.append(text
    return longest[-1]
