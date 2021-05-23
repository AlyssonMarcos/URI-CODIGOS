A, B, C = input().split(' ')
A = int(A)
B = int(B)
C = int(C)

maiorAB = (A + B + abs(A - B)) / 2  # funcão abs sempre retorna o valor positivo da operação

if maiorAB > C:
    print(f'{int(maiorAB)} eh o maior')  # o resultado deve ser sempre inteiro
else:
    print(f'{C} eh o maior')
