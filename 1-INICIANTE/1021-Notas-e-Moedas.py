noteValue = float(input())

# Valores de notas e moedas para decompor na variavel noteValue
notes = ['100', '50', '20', '10', '5', '2']
coins = ['1', '0.50', '0.25', '0.10', '0.05', '0.01']

# Objetos iniciais para armazenar a quantidade de notas e moedas
amountNotes = {}
amountCoins = {}

for note in notes:
    amountNotes[note] = int(noteValue / int(note))
    noteValue -= amountNotes[note] * int(note)

for coin in coins:
    amountCoins[coin] = int(noteValue / float(coin))
    # A função round arredonda para cima e resolve o nosso problema de subtração.
    # exemplo: 0.3 - 0.1 = 0.19999999999999998 ao inves de 0.2
    noteValue = round(noteValue - amountCoins[coin] * float(coin), 2)

print('NOTAS:')
for note in notes:
    print(f'{amountNotes[note]} nota(s) de R$ {float(note):.2f}')

print('MOEDAS:')
for coin in coins:
    print(f'{amountCoins[coin]} moeda(s) de R$ {float(coin):.2f}')
