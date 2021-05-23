values = list(map(int, input().split()))
position = 1
total_sum = 0

while values[position] <= 0:
    position += 1
    if values[position] > 0:
        break

for i in range(0, values[position]):
    total_sum = total_sum + values[0] + i

print(total_sum)
