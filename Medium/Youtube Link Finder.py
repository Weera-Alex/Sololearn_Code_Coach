link = input()
a = False
b = ""
if "youtube" in link:
    for x in link:
        if x == "=" or a:
            a = True
            if x == "=":
                continue
            else:
                b += x
                print(x,end="")
elif "youtu.be" in link:
    for x in link:
        if x == "/":
            if a:
                a = False
            else:
                a = True
        elif a:
            b += x
            print(x, end="")