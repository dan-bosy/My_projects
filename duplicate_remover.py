def remove_duplicates(lst):
    prev_num = []
    for num in lst:
        if num not in prev_num:
            prev_num.append(num)
    return prev_nu
