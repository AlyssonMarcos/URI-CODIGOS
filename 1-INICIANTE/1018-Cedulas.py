note_value = int(input())
new_note_value = note_value
# Valores de notas para decompor na variavel noteValue
notes = ['100', '50', '20', '10', '5', '2', '1']

# Objeto inicial para armazenar a quantidade de notas
amountNotes = {}

for note in notes:
    amountNotes[note] = int(new_note_value / int(note))
    new_note_value -= amountNotes[note] * int(note)

print(note_value)
for note in notes:
    print(f'{amountNotes[note]} nota(s) de R$ {note},00')
