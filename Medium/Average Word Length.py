import math
import string

a = input()
b = len(a)

counter = 0
divider = 1
for x in a:
    if x in string.ascii_letters:
        counter += 1
    elif x == " ":
        divider += 1
print(math.ceil(counter / divider))