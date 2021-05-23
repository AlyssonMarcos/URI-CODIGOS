litros_KM = 12  # Quantidade de litros de combustível gastos por quilometros
tempo_gasto_HR = int(input())
velocidade_media = int(input())

litros_necessario = (tempo_gasto_HR * velocidade_media) / litros_KM

print(f'{litros_necessario:.3f}')
