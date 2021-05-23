user = int(input())

for column1 in range(1, user + 1):
    colunm2 = column1 * column1
    colunm3 = column1 * colunm2
    print(f'{column1} {colunm2} {colunm3}')
