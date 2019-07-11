"""
054
Crie um programa que leia o ano de nascimento de ste pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores
Considere maioridade = 21 anos
"""
from datetime import date

maiorIdade = 21
diMenor = 0
diMaior = 0
Nascimentos = [1996, 2000, 2015, 1990, 1985, 2012, 2007]
for i in range(len(Nascimentos)):
    #anoNascimento = int(input("Digite seu ano de nascimento: "))
    idade = date.today().year - Nascimentos[i]
    if idade < maiorIdade:
        diMenor += 1
    else:
        diMaior += 1

print("{} pessoas atingiram a maior idade e outras {} ainda são dimenores".format(diMaior, diMenor))