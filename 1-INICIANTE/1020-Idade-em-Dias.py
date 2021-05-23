dias = int(input())

anos = dias // 365
dias -= (anos * 365)
mes = dias // 30
dias -= (mes * 30)

print(f'''{anos} ano(s)
{mes} mes(es)
{dias} dia(s)''')
