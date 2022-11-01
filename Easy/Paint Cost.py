canvas_and_brushes = 40
paint_cost = 5
paints_needed = int(input())
total = paints_needed * paint_cost + canvas_and_brushes
tax = 0.10 * total
print(round(total + tax))
