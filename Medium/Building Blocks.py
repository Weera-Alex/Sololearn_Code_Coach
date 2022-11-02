block = []
for x in range(4):
    block.append(int(input()))
while block[0] >= 15:
    block[0] = block[0] - 15
while block[1] >= 15:
    block[1] = block[1] - 15
while block[2] >= 15:
    block[2] = block[2] - 15
while block[3] >= 15:
    block[3] = block[3] - 15
print(sum(block))