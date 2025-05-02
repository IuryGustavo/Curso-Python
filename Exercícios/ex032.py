'''
Faça um programa que leia um ano qualquer e
mostre se ele é BISSEXTO.
'''
from datetime import date

print('Ano 0 corresponde ao ano atual da maquina.')
ano = int(input('Qual ano deseja analiazar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
