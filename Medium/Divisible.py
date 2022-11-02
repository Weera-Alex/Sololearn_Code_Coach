number = int(input())
divisor = input().split()
lock = 1
for x in divisor:
    if number % int(x) != 0:
        print("not divisible by all")
        lock = 0
        break
if lock:
    print("divisible by all")