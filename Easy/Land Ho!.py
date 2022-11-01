line = int(input())
waiting_time = 10
while line >= 20:
    waiting_time += 20
    line -= 20
print(waiting_time)
