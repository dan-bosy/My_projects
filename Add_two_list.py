l1 = [2,4,3]
l2 = [5,6,4]
l3 = [str(x) for x in l1]
l4 = [str(x) for x in l2]
final_l = []

l3.reverse()
l4.reverse()
l5 = ''.join(l3)
l6 = ''.join(l4)

total_str = str(int(l5)+int(l6))
total_str = total_str[::-1]
total_str = list(total_str)

print(total_str)
