'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem ou SILVA no nome.
'''

nome = input('Digite seu nome: ').strip()
print(f'Seu nome tem Silva: {'SILVA' in nome.upper()}')
