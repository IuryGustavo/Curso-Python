'''
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece pela primeira vez.
Em que posição ela aparece pela ultima vez.
'''

frase = input('Digite algo: ').upper().strip()
print(f'Quantas vezes aparece a letra "A": {frase.count('A')}')
print(f'Posição que aparece pela primeira vez: {frase.find('A')+1}')
print(f'Posição que aparece pela ultima vez: {frase.rfind('A')+1}')
