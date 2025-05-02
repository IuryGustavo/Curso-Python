'''
Faça um programa que leia o nome completo de uma pessoa,
mostre em seguida o primeiro e o último nome separadamente.
'''

nome = input('Digite seu nome: ').strip()
separado = nome.split()
print(f'Seu primeiro nome: {separado[0]}')
print(f'Seu último nome : {separado[len(separado)-1]}')
