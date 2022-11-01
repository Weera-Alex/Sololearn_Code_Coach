numbers = int(input())
num = []
for x in range(numbers - 1, 1, -1):
    if x % 3 == 0:
        num.append(x)


for x in range(numbers - 1, 1, -1):
    if x % 5 == 0 and x not in num:
        num.append(x)

print(sum(num))
