import copy
us_date = input()
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
if us_date[0].isnumeric():
    us_date = us_date.split("/")
    copylist = copy.deepcopy(us_date)
    us_date[0] = copylist[1]
    us_date[1] = copylist[0]
    new_date = ""
    for x in us_date:
        new_date += x + "/"
    print(new_date[:-1])
else:
    us_date = us_date.replace(",", "").split()
    us_date[0] = str(dict[us_date[0]])
    copylist = copy.deepcopy(us_date)
    us_date[0] = copylist[1]
    us_date[1] = copylist[0]
    new_date = ""
    for x in us_date:
        new_date += x + "/"
    print(new_date[:-1])

