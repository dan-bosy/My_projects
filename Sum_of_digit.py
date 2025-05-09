def sum_of_digits(num):
    digit_sum = 0
    int_to_str = [x for x in str(num)]
    str_to_int = [int(c) for c in int_to_str]
    for n in str_to_int:
       digit_sum += n
    return digit_sum
