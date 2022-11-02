num = int(input())
initial = ""
for x in range(num):
    name = input().split()
    for x in name:
        initial += x[0]
    initial += " "
print(initial)