apartment_a = input()
apartment_b = input()
a = apartment_a.split(",")
b = apartment_b.split(",")
a_size = int(a[0]) * int(a[1])
b_size = int(b[0]) * int(b[1])
if a_size > b_size:
    print("Apartment A")
else:
    print("Apartment B")
