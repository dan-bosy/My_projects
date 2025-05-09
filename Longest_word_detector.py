def longest_word(sentence):
    max_len = []
    for word in sentence.split():
        max_len.append(len(word))
    
    for word2 in sentence.split():
        if len(word2) == max(max_len):
            
            return word2
            brea
