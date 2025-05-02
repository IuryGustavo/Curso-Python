'''
Crie um programa que faça o computador
jogar Jokenpô com você.
'''

from random import choice
from time import sleep

print('\033[1;32m-=-'*7)
print(f'\033[1;33m{'Jokenpô':^20}')
print('\033[1;32m-=-\033[m'*7)
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(jokenpo)
jogador = input('Pedra, Papel ou Tesoura: ').upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*20)
print(f'Jogador jogou {jogador}')
print(f'Computador jogou {computador}')
print('-='*20)
if computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('\033[34mÉ isso aí, eu venci!!!')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('\033[34mIsso aí, eu venci!!!')
elif computador == 'PEDRA' and jogador == 'PAPEL' or computador == 'TESOURA' and jogador == 'PEDRA':
    print('\033[32mParabéns você venceu! ):')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print('\033[32mParabéns, você venceu! ):\033[m')
elif computador == 'PEDRA' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'TESOURA':
    print('Empate, mais uma vez agora eu te venço')
elif computador == 'PAPEL' and jogador == 'PAPEL':
    print('Empate, mais uma vez agora eu venço')
else:
    print('\033[31mO jogo é Jokenpô, não tente inventar!!!')
