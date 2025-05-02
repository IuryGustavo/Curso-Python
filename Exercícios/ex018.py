'''
Faça um program que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
import math

angulo = int(input('Digite o ângulo: '))
rad = math.radians(angulo)
print(f'O seno: {math.sin(rad):.1f}\nO cosseno: {math.cos(rad):.1f}\nA tangente: {math.tan(rad):.1f}')
