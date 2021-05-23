A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
PI = 3.14159

area = {
    "triangulo": (A * C) / 2,
    "circulo": PI * (C ** 2),
    "trapezio": ((A + B) * C) / 2,
    "quadrado": B ** 2,
    "retangulo": A * B
}

print(f"""TRIANGULO: {area['triangulo']:.3f}
CIRCULO: {area['circulo']:.3f}
TRAPEZIO: {area['trapezio']:.3f}
QUADRADO: {area['quadrado']:.3f}
RETANGULO: {area['retangulo']:.3f}""")
