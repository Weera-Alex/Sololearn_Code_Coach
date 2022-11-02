numbers = input().split()
numbers = [float(x) * 0.1 + float(x) for x in numbers]
lock = 1
for x in numbers:
    if x >= 20:
        print("Back to the store")
        lock = 0
        break
if lock:
    print("On to the terminal")