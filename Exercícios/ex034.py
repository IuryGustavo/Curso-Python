'''
Escreva um programa que pergunte o salário de um funcionario e
calcule o valor do seu aumento. Para salários superiores a 1250,
calcule um aumento de 10%. Para inferiores ou iguais, o aumento
é de  15%.
'''

salario = float(input('Qual o seu salário: '))
if salario<=1250:
    print(f'Seu salário com o aumento é {salario*0.15 + salario}')
else:
    print(f'Seu salário com aumento é {salario*0.1 + salario}')
