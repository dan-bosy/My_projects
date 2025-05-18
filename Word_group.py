def group_by_length(words):
    group1 = {}
    group2 = {}
    for word in words:
        if word in group1:
            group1[word] += len(word)
        else:
            group1[word] = len(word)
    for key, value in group1.items():
        if value not in group1:
            group2[value] = key
        else:
            group2.update({value:key})
    return group
