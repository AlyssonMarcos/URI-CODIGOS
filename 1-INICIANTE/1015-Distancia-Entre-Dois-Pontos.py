from math import sqrt
p1 = list(map(float, input().split()))  # x1 e y1
p2 = list(map(float, input().split()))  # x2 e y2

x = (p2[0] - p1[0]) ** 2
y = (p2[1] - p1[1]) ** 2

distancia = sqrt(x + y)

print(f'{distancia:.4f}')
