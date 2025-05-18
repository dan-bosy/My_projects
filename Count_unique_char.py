def count_unique_characters(s):
    count = 0
    seen_char = ''
    for char in s.lower():
        if char not in seen_char and char != ' ':
            seen_char += char
            count += 1
    return count
