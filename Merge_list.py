def merge_sorted_lists(lst1, lst2):
    merged_list = []
    for num1 in lst1:
        merged_list.append(num1)
    for num2 in lst2:
        merged_list.append(num2)
        
    return sorted(merged_list)
