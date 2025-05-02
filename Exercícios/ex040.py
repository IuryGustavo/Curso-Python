'''
Crie um progra a que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com sua média atingida:
-Média abaixo de 5.0: Reprovado
-Media entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: aprovado
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print(f'Com as notas {nota1} e {nota2} a média é {media}')
if media < 5:
    print(f'\033[1;31mVocê está reprovado com a média {media:.1f}, mais sorte da proxima vez.')
elif 5 <= media < 7:
    print(f'\033[1;33m Você está de recuperação com média {media:.1f}, estude mais.')
else:
    print(f'\033[1;32m Você está aprovado com média {media:.1f}, parabéns!!!')
