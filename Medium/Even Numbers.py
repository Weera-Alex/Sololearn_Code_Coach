numbers = input().split()
new_numbers = ""
for x in numbers:
    if int(x) % 2 == 0:
        new_numbers += x + " "
print(new_numbers)