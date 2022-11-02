import math
numbers = input().split(",")
num = [float(x) for x in numbers]
sale_ava = sum(num) - max(num)
tax = sale_ava * 0.07
total = (sale_ava + tax) * 0.03 * 10
print(math.floor(total))
