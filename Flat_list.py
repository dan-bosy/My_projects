def flatten_list(lst):
    flat_lst = []
    for num in lst:
        if type(num) == list:
            
            for num2 in num:
                if type(num2) == list:
                    
                    for num3 in num2:
                        flat_lst.append(num3)
                else:
                    flat_lst.append(num2)
        else:
            flat_lst.append(num)
      
    return flat_lst


print(flatten_list([1, [2, 3], [4, [5, 6]]])
