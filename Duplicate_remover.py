def remove_duplicates(nums):
    unique_nums = []
    second_unique = []
    cleaned_nums = max(nums) + 1
    iter_cleaned = [x for x in range(1, cleaned_nums)]  

    for num in nums:
        if num in iter_cleaned:
            unique_nums.append(num)
            
    for num in unique_nums:
        if num not in second_unique:
            second_unique.append(num)
            
    return second_unique
