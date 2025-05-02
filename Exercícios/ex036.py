'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele
vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado
'''

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos irá pagar: '))
mensalidade = casa/(anos*12)
print(f'Valor da mensalidade é R${mensalidade:.2f}')
if mensalidade < salario*0.3:
    print(f'Seu emprestimo foi aprovado')
else:
    print(f'Seu empretimo foi negado, a mensalidade é maior que 30% do seu salário')
