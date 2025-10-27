'''
Faça um programa que faça uma contagem 
regressiva com espera de 1 segundo
'''

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)