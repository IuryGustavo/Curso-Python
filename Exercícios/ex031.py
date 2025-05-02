'''
Desenvolva um programa que pergunte a distância de uma
viagem em km. Calcule o preço da passagem, combrando R$0,50
por km para viagens até 200km e R$0,45 para viagens mais longas.
'''

distancia = int(input('Distância da viagem em km:'))
if distancia <= 200:
    print(f'O valor da passagem será R${distancia*0.5:.2f}')
else:
    print(f'O valor da passagem será R${distancia*0.45:.2f}')
