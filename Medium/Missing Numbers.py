number = int(input())
unique = set()
for x in range(number):
    unique.add(int(input()))
sort = sorted(unique)
new_uniq = set()
for x in range(min(sort), max(sort) + 1):
    new_uniq.add(x)
for x in new_uniq:
    if x not in sort:
        print(x, end=" ")
