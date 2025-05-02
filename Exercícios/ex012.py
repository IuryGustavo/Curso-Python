'''
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
'''

prod = float(input('Valor do produto: R$'))
print(f'O novo valor do produto com 5% é R${prod-prod*0.05:.2f}.')
