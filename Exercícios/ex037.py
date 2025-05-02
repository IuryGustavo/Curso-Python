'''
Escreva um programa que leia um número inteiro qualquer e peça
para o usúario escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadrcimal
'''

numero = int(input('Digite um número: '))
print('''Escolha uma das bases:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
conv = int(input('Sua opção: '))
if conv == 1:
    print(f'{numero} convertido para Binário é {bin(numero)[2:]}')
elif conv == 2:
    print(f'{numero} convertido para Octal é {oct(numero)[2:]}')
elif conv == 3:
    print(f'{numero} convertido para Hexdecimal é {hex(numero)[2:]}')
else:
    print('\033[1;31mDigite um dos números acima para fazer a conversão')
