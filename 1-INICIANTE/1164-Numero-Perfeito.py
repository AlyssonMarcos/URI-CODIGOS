def divisor(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)

    return divisores


quantidade_entradas = int(input())

for qtd_entrada in range(quantidade_entradas):
    numero_perfeito = int(input())
    divisores = divisor(numero_perfeito)

    if sum(divisores) == numero_perfeito:
        print(f'{numero_perfeito} eh perfeito')
    else:
        print(f'{numero_perfeito} nao eh perfeito')
