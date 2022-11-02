num = int(input())
number = [0]
test = 1
for x in range(num):
    no = int(input())
    if sum(number) > no:
        test = 0
    number.append(no)
if test:
    print("true")
if not test:
    print("false")