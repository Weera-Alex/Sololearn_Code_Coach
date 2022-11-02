mine = input().split(",")
need = input()
count = 1
for mining in mine:
    if mining == need:
        print(count * 5)
    count += 1

