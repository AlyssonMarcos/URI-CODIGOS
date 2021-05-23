# A logica do programa é a razão igual a 4

user = int(input())
numberSequence = [1, 2, 3]

for pum in range(0, user):
    print(f'{numberSequence[0]} {numberSequence[1]} {numberSequence[2]} PUM')
    numberSequence[0] += 4
    numberSequence[1] += 4
    numberSequence[2] += 4

