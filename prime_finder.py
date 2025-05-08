def find_primes_in_range(start, end):
    primes_list = []
    for num in range(start, end):
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes_list.append(num)
    return primes_lis
