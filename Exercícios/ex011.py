'''
Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a área e a quantidade de tinta
necessária para pinta-lá sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados.
'''

larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
print(f'Será necessário {larg*alt/2}l de tinta para pintar uma parede com {larg*alt} metros quadrados.')