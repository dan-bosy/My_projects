def sum_of_digits(s):
    cleaned = [int(x) for x in s if x.isdigit()]
    total = 0
    for num in cleaned:
        total += num
    return total
