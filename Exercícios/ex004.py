'''
Crie um programa que leia algo pelo teclado e msotre na tela o seu tipo primitivo
e todas as suas informações possiveis sobre ele.
'''

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabetico? {algo.isalpha()}')
print(f'É alfanumerico? {algo.isalnum()}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'Está somente em letras minusculas? {algo.islower()}')
print(f'Está somente em letras maiusculas? {algo.isupper()}')
print(f'Está capitalizado? {algo.istitle()}')
