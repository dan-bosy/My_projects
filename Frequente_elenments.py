def most_frequent_element(lst):
    dict_count = {}
    dict_value = []
    for num in lst:
        if num in dict_count:
            dict_count[num] += 1
        else:
            dict_count[num] = 1
    for value in dict_count.values():
        dict_value.append(value)
        
    for key, value in dict_count.items():
        if value == max(dict_value):
            return key
            break
