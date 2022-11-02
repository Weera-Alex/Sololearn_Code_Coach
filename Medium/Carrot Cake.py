your_carrot = int(input())
number_of_boxes = int(input())
total = number_of_boxes % your_carrot
while your_carrot > total:
    your_carrot = your_carrot - number_of_boxes
if 7 - your_carrot <= 0:
    print("Cake Time")
else:
    print(f"I need to buy {7 - your_carrot} more")