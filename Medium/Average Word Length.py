import math
import string
counter = 0
divider = 1
for x in input():
    if x in string.ascii_letters:
        counter += 1
    elif x == " ":
        divider += 1
print(math.ceil(counter / divider))