def longest_word(text):
    max_len = []
    words = text.split()
    for word in words:
        max_len.append(len(word))
    for char in words:
        if len(char) == max(max_len):
            return char
