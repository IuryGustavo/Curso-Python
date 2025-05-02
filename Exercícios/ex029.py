'''
Escreva um programa que leia a velocidade de um carro.
Se ele utrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multador. Amulta vai custar R$7,00 por
cada km acima do limite.
'''

km = int(input('Velocidade do carro em km: '))
if km > 80:
    print('Você exedeu o limite de velocidade permitida')
    print(f'Terá que pagar uma multa de  R${(km-80)*7:.2f}')
print('Dirija com cuidado')
