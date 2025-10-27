'''
Faça um programa que exiba na tela a soma de 
todos os números ímpares multiplos de 3, entre 1 e 500.
'''
soma_imp = 0

for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma_imp += impares

print(f"A soma de todos os números solicitados é {soma_imp}")
