'''
Faça um programa que leia o ano de nascimento de
um jovem e informe, de acordo com a sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa também deve mostrar o tempo que
faltou ou que passou do prazo
'''

from datetime import date

nasc = int(input('Em qual ano você nasceu: '))
atual = date.today().year
idade = atual-nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Já está na hora de se alistar.')
elif idade < 18:
    print(f'Você ainda vai ter que se alista, falta {18-idade} anos')
    print(f'Seu alistamento vai ser em {atual+(18-idade)}')
else:
    print(f'Você já deveria te há {idade-18} anos')
    print(f'Seu alistamento foi em {atual-(idade-18)}')