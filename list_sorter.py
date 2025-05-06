def sort_colors(lst):
    result = []
    max_index = max(lst) + 1
    numbers = [x for x in range(max_index)]
    for i in numbers:
            for j in lst:
                if j == i:
                    result.append(j)
    print(result)
    
