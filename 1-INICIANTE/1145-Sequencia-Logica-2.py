x, y = input().split(' ')
x, y = int(x), int(y)

newX = x
for num in range(1, y + 1):
    if num == newX:
        print(num, end='')
        print()
        newX += x
    else:
        print(num, end=' ')
