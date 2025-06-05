nums = [0,1,0, 3, 12]
fix_nums = [x for x in nums if x != 0]
zeros = [n for n in nums if n == 0]
len_numbers = len(fix_nums)
nums = sorted(fix_nums)
for empty in zeros:
    nums.append(empty)
