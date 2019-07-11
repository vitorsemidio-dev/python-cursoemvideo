"""
047
Crie um programa que mostre na tela todos os numeros pares entre 1 e 50
"""
inicio = 1
fim = 50
passo = 2

if inicio % 2 != 0:
    inicio += 1

for i in range(inicio, fim+1, passo):
    print("{}".format(i))
