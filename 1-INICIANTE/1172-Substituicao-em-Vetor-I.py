x = []

for i in range(0, 10):
    try:
        userValue = int(input())
        x.append(userValue)

        if x[i] <= 0:
            x[i] = 1
    except:
        x.append(1)
        continue

for key, valueArray in enumerate(x):
    print(f'X[{key}] = {valueArray}')
