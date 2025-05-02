'''
faça um programa que leia um número de 0 a
9999 e mostre na tela cada um dos digitos separados.
'''

numero = int(input('Digite um número 0-9999: '))
print(f'Esse número tem:\n{numero//1%10} Unidades\n{numero//10%10} Dezenas')
print(f'{numero//100%10} Centena\n{numero//1000%10} Unidade de Milhar')
