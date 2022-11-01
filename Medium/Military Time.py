a = input()
b = ""
if "AM" in a:
    x = a.replace("AM", "")
    print(x)
elif "PM" in a:
    x = a.replace("PM", "")
    dict = {
        1: 13,
        2: 14,
        3: 15,
        4: 16,
        5: 17,
        6: 18,
        7: 19,
        8: 20,
        9: 21,
        10: 22,
        11: 23,
        12: 24
    }
    for c in x:
        if c == ":":
            break
        b += c
    print(dict[int(b)],(x[-4] + x[-3] + x[-2]),sep="")