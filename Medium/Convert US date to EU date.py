a = input()
count = 0
b = ""
c = ""
d = ""
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
y = ""
t = ""
year = ""
ti = True
t2 = False
if a[0].isnumeric():
    for x in a:
        if count == 2:
            d += x
        if x == "/":
            count += 1
        if count == 0 and x != "/":
            b += x
        if count == 1 and x != "/":
            c += x
    print(c, b, d, sep="/")

else:
    for x in a:
        if x.isnumeric() and t2:
            year += x
        if x.isnumeric() and ti:
            y += x
        if x == ",":
            ti = False
            t2 = True
        elif x != " " and not x.isnumeric():
            t += x

    print(y,dict[t],year,sep="/",end="")