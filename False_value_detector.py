def remove_false_values(lst):
    cleaned_lst = [item for item in lst if item != '' and item != False and item != 0 and item != None and item != []]
    return cleaned_lst


print(remove_false_values([0, 1, False, 2, "", None, 3, [], 4]))
