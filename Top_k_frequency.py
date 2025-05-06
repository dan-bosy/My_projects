def top_k_frequent(lst, num):
    count = {}
    result = []
    for n in lst:
        if n in count:
            count[n] += 1
        else:
             count[n] = 1
    for key, value in count.items():
         if value > 1:
             result.append(key)
         elif key == num:
              result.append(key)
    print(result)
  
