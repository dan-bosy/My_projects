    
nums = [3, 0, 1, 5, 7]
full_numbers = max(nums)
missed_num = []
for num in range(full_numbers):
    if num not in nums:
        missed_num.append(num)
