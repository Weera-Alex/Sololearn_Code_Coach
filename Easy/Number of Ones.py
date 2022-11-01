number = bin(int(input()))[2:]
b = 0
for x in str(number):
    b += int(x)
print(b)
