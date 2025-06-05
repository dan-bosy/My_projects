def merge_sorted_lists(list1, list2):
    merged_list = []
    for num1 in list1:
        merged_list.append(num1)
    for num2 in list2:
        merged_list.append(num2)
        
    return sorted(merged_list)
