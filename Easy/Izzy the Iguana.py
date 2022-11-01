snacks = input().split()
points = 0
for x in snacks:
    if x == "Lettuce":
        points += 5
    if x == "Carrot":
        points += 4
    if x == "Mango":
        points += 9
if points >= 10:
    print("Come on Down!")
else:
    print("Time to wait")
