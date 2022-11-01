import string
alpha = string.ascii_lowercase
reverse = alpha[::-1]
reverse = list(reverse)
alpha = list(alpha)
res = dict(zip(alpha, reverse))
text = input().lower()
for x in text:
    if x != " ":
        print(res[x], end="")
    elif x == " ":
        print(" ", end="")
        