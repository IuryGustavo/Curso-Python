'''
Elabore um programa que calcule o valor a ser pago por um 
produto, considerando o seu preço normal e condição de pagamento: 
-À vista dinheiro ou cheque:10% de desconto 
-À vista no cartão:5% de desconto 
-Em até 2x no cartão:preço normal 
-3x ou mais no cartão:20% de juros
'''

preço = float(input('Preço das compras: R$'))
print('''Método de Pagamento
[ 1 ] Á vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
metodo = int(input('Qual forma de pagamento: '))
if metodo == 1:
    print(f'O preço da compra com o desconto de 10% é R${preço-(preço*0.1):.2f}')
elif metodo == 2:
    print(f'O preço da compra com desconto de 5% é R${preço-(preço*0.05):.2f}')
elif metodo == 3:
    print(f'A sua compra será parcelada 2x de R${preço/2:.2f}')
elif metodo == 4:
    parcelas = int(input('Quantas parcelas: '))
    print(f'Sua compra será parcelada {parcelas}x de R${(preço+(preço*0.2))/parcelas:.2f}')
    print(f'Sua compra custava {preço} com o juros de 20% passa a custar R${preço+(preço*0.2)}')
else:
    print('Não tem esse método de pagamento disponível')

