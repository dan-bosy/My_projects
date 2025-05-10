def non_repeated_char(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for key, value in count.items():
            if value == 1:
                return key
    return None
        
print(non_repeated_char("swiss")
