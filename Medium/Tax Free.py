number = input().split(",")
number = [int(x) for x in number]
tax = 0
for x in number:
    if x < 20:
        tax += x * 0.07
print(sum(number) + tax)