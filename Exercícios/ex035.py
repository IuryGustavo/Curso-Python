'''
Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um triângulo.
'''

print('--=--'*5)
print('Analisador de Triângulos')
print('--=--'*5)
lado1 = float(input('Primeira reta: '))
lado2 = float(input('Segunda reta: '))
lado3 = float(input('Terceira reta: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Essas três retas podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')
