card_number = input()[::-1]
beep_boop = 1
new_number = []
for number in card_number:
    if not beep_boop:
        new_number.append(int(number) * 2)
        beep_boop = 1
    else:
        new_number.append(int(number))
        beep_boop = 0


low_number = []
for large in new_number:
    if large >= 10:
        low_number.append(large - 9)
    else:
        low_number.append(large)
print(sum(low_number))
if sum(low_number) % 10 == 0 and len(card_number) == 16:
    print("valid")
else:
    print("not valid")