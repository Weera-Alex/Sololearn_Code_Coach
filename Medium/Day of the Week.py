import datetime
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
date = input()
if "/" in date:
    date = date.split("/")
    date = [int(x) for x in date]
    x = datetime.datetime(date[2], date[0], date[1])
    print(x.strftime("%A"))
else:
    date = date.replace(",", "").split()
    date[0] = dict[date[0]]
    x = datetime.datetime(int(date[2]), date[0], int(date[1]))
    print(x.strftime("%A"))
