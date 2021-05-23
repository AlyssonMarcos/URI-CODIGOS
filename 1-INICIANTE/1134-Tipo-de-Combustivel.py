alcool = 0
gasolina = 0
diesel = 0
fim = 0

"""print('-='*6)
print('''1 => Álcool
2 => Gasolina 
3 => Diesel 
4 => Fim)''')
print('-='*6) """

while True:
    user = int(input())

    if user == 1:
        alcool += 1
    elif user == 2:
        gasolina += 1
    elif user == 3:
        diesel += 1
    elif user == 4:
        break

print(f'''MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}''')
