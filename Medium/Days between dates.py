from datetime import date
dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

first = input().replace(",", "").split()
second = input().replace(",", "").split()
first[0] = dict[first[0]]
second[0] = dict[second[0]]
f_date = date(int(first[2]), first[0], int(first[1]))
l_date = date(int(second[2]), second[0], int(second[1]))
delta = l_date - f_date
print(delta.days)
