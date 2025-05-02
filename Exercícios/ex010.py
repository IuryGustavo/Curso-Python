'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
1US$ = 5,45R$
'''

reais = float(input('Quantos reais você tem: R$'))
print(f'Com {reais:.2f}R$ você pode comprar {reais/5.45:.2f}US$')
