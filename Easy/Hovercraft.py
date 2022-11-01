hovercrafts = 10
cost = 2000000
insurance = 1000000
expenses = hovercrafts * cost + insurance
customer = int(input())
sold = expenses - customer * 3000000
if sold == 0:
    print("Broke Even")
elif sold > 0:
    print("Loss")
else:
    print("Profit")
