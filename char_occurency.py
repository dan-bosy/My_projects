def count_char_occurrences(s):
    dict_count = {}
    for char in s:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count

