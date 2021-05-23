resultado_s = 1
dividendo = 3
divisor = 2

for i in range(13):
    resultado_s += (dividendo / divisor)
    dividendo += 2
    divisor *= 2
print(f'{resultado_s:.2f}')
