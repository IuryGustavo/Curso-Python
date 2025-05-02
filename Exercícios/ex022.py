'''
Crie um programa que leia o nome de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras tem (sem considerar espaços).
Quanstas letras tem o primeiro nome.
'''

nome = input('Digite seu nome: ')
print(f'Com letras maiúsculas: {nome.upper()}')
print(f'Com letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome.replace(' ', ''))}')
separado = nome.split()
print(f'Quantidade letras primeiro nome: {len(separado[0])}')
