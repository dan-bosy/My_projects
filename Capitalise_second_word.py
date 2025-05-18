def capitalize_alternate(sentence):
    words = sentence.split()
    for c in range(len(words)):
        if c % 2 == 1:
            words[c] = words[c].upper()
            
    return ' '.join(words)
