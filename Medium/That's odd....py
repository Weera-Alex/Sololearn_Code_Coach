n = int(input())
x = []
for y in range(n):
    x.append(int(input()))

c = 0
for a in x:
    if a % 2 == 0:
        c += a
print(c)
