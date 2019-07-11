"""
086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha os valores lidos pelo teclado
No final, mostre a matriz na tela, com a formatação correta
"""
from random import randint

dimensao = int(input("Digite a dimensão da matriz: "))

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"[{matriz[i][j]:^5}]", end=" ")
        print("")

#Cria matriz quadrada de dimensao N
matriz = []
for i in range(dimensao):
    matriz.append([])
    for j in range(dimensao):
        matriz[i].append(0)



#Preenche os valores da matriz de dimensao N
for i in range(dimensao):
    for j in range(dimensao):
        matriz[i][j] = randint(0, 100)

#Imprime a matriz de maneira formatada
printMatriz(matriz)