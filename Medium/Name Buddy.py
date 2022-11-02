name = input().split()
your_name = input()
lock = 1
for x in name:
    if your_name[0] == x[0]:
        print("Compare notes")
        lock = 0
        break
if lock:
    print("No such luck")
