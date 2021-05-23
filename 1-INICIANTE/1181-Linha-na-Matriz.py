linha_operacao = int(input())  # linha do array que será feita a operação
operacao_realizar = input()  # S para soma ou M para media

matrix = []

# valor padrão para manipulação da matrix
valor_padrao_matrix = 12

for _ in range(valor_padrao_matrix):
    matrix.append([" "] * valor_padrao_matrix)

for i in range(valor_padrao_matrix):
    for j in range(valor_padrao_matrix):
        matrix[i][j] = float(input())


def operacao(linha, caractere_operacao):
    valores_linha = matrix[linha]
    resultado = 0
    tamanho_array = len(valores_linha)  # será usado para tirar a media

    for valor in valores_linha:
        resultado += valor

    if caractere_operacao == 'S':
        return resultado
    elif caractere_operacao == 'M':
        return resultado / tamanho_array


print(operacao(linha_operacao, operacao_realizar))