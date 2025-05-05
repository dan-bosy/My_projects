def sort_colors(lst):
    sorted = []
    max_index = max(lst) + 1
    numbers = [x for x in range(max_index)]
    for i in numbers:
            for j in lst:
                if j == i:
                    sorted.append(j)
    print(sorted)
    
