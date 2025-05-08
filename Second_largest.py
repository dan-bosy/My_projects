def second_largest(lst):
    second_largest_num = sorted(set(lst))[::-1]
  
    return second_largest_num[1] if len(second_largest_num) >= 2 else None
