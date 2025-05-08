def common_elements(lst1, lst2):
    common_list = []
    for item in lst1:
        if item in lst2:
            common_list.append(item)
            
    return common_list
