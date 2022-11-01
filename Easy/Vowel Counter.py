b = 0
for x in input().upper():
    b += x.count("A")
    b += x.count("E")
    b += x.count("O")
    b += x.count("I")
    b += x.count("U")
print(b)