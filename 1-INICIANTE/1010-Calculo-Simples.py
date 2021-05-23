produto_1 = input().split(' ')
produto_1[0] = int(produto_1[0])  # codigo da peça
produto_1[1] = int(produto_1[1])  # qunatidade de peças
produto_1[2] = float(produto_1[2])  #valor unitario

produto_2 = input().split(' ')
produto_2[0] = int(produto_2[0])
produto_2[1] = int(produto_2[1])
produto_2[2] = float(produto_2[2])

total = (produto_1[1] * produto_1[2]) + (produto_2[1] * produto_2[2])

print(f'VALOR A PAGAR: R$ {total:.2f}')
