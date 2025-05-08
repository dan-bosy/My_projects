def convert_to_dict(lst):
    result_dict = {}
    int_lst = []
    str_lst = []
    for item in lst:
        for i in item:
            if type(i) == int:
                int_lst.append(i)
            else:
                str_lst.append(i)
    for key, value in zip(str_lst, int_lst):
        result_dict[key] = value
  
    return result_dict

