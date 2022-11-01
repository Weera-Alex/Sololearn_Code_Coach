import math
height_door = int(input())
weight_door = int(input())
door = height_door * weight_door * 2
duct = (60 / 12) * 2
print(math.ceil(door/duct))
