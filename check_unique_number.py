nums = [4, 1, 2, 1, 2, 4, 9]
counter = {}
for n in nums:
      if n not in counter:
          counter[n] = 1
      else:
          counter[n] += 1
      
for number, amount in counter.items():
      if amount == 1:
          print(number)
