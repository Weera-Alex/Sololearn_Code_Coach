Kaleidoscopes = int(input())
if Kaleidoscopes > 1:
    discount = Kaleidoscopes * 0.10
    total = (Kaleidoscopes - discount) * 5
    tax = total * 0.07
    print(round(total + tax, 2))
else:
    total = Kaleidoscopes * 5
    tax = total * 0.07
    print(round(total + tax, 2))
