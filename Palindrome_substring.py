def longest_palindromic_substring(lst):
    palin = ''
    rev_lst = list(lst[::-1])
    convert_to_list = list(lst)
    for key, value in zip(rev_lst, convert_to_list):
        if key == value:
            palin += key
    print(palin)
    
