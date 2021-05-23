nome = input()
salario_fixo = float(input())
vendas_efetuadas = float(input())
comisao = 0.15  # 15%

total = salario_fixo + (vendas_efetuadas * comisao)

print(f'TOTAL = R$ {total:.2f}')
