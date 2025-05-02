'''
Escreva um programa que faça o computador "pensar" em um número 
inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi 
o número escolhido pelo computador. O programa deverá escrevaer na 
tela se o usuário venceu ou perdeu.
'''

from random import randint

n0a5 = randint(0, 5)
print('\033[32m--=--'*9)
print('\033[1;33mTente acertar o número escolhido entre 0 e 5')
print('\033[32m--=--\033[m'*9)
chute = int(input('Qual é o número: '))
if chute == n0a5:
    print('\033[33mParabéns! Você acertou.\033[m')
else:
    print(f'\033[31mVocê não acertou o número escolhido foi {n0a5} e não {chute}\033[m')
