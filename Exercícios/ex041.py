'''
A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Até 9 anos: Mirin
-Até 14 anos:Infantil
-Até 19 anos: Junior
-Até 25 anos:Sênior
-Acima: Master
'''

from datetime import date

nasc = int(input('Em qual ano você nasceu: '))
idade = date.today().year - nasc
if idade <= 9:
    print(f'É um atleta Mirin com {idade} anos')
elif idade <= 14:
    print(f'É um atleta Infantil com {idade} anos')
elif idade <= 19:
    print(f'É um atleta Junior com {idade} anos')
elif idade <= 25:
    print(f'É um atleta Sênior com {idade} anos de idade')
else:
    print(f'É um atleta Master com {idade} anos')
