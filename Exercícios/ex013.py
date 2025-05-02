'''
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de almento.
'''

sal = float(input('Digite o salário: R$'))
print(f'O salário com o reajuste de 15% fica R${sal+sal*0.15:.2f}.')
