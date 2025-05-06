
def find_missing_number(lst):
    max_number = max(lst) + 1
    lst_index = [x for x in range(1,max_number)]
    result = []
    
    for num in lst_index:
        if num not in lst:
            result.append(num)
    print(result)
