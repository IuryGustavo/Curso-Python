'''
Refaça o desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triangulo será formado:
-Equilatero
-Isósceles
-Escaleno
'''

print('\033[1;32m--=--'*5)
print('\033[1;33mAnalizador de Triângulo')
print('\033[1;32m--=--\033[m'*5)
lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))
if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    print('Os segmentos podem formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('Esses segmentos formam um triângulo EQUILATERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('Esses segmentos formam um triângulo ESCALENO')
    else:
        print('Esses segmentos formam um triângulo ISÓCELES')
else:
    print('Os segmentos não podem formar um triângulo')
