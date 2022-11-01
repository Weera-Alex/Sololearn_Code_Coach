food_menu = {
    "Nachos": 6,
    "Pizza": 6,
    "Cheeseburger": 10,
    "Water": 4,
    "Coke": 5,
}
order = input().split()
cost = 0
for each_order in order:
    if each_order in food_menu:
        cost += food_menu[each_order]
    else:
        cost += 5
tax = 0.07 * cost
print(cost + round(tax, 2))
