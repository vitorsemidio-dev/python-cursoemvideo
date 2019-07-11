"""
087
Aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados.
b) a soma dos valores da terceira coluna.
c) o maior valor da segunda linha.
"""
from random import randint
dimensao = int(input("Digite a dimensão da matriz: "))
#dimensao = randint(2,10)

def somaPares(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                soma += matriz[i][j]
    return soma

def somaColunaX(matriz, coluna):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][coluna-1]
    return soma

def maiorLinhaX(matriz, linha):
    maior = max(matriz[linha-1])
    return maior

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

sumPares = somaPares(matriz)
coluna = 3
linha = 2

#Aleatorio
#coluna = randint(0,dimensao)
#linha = randint(0,dimensao)



print(f"A soma de todos os pares digitados foi {sumPares}")
coluna = 3
print(f"A soma de todos os elementos da coluna {coluna} foi {somaColunaX(matriz, coluna)}")
linha = 2
print(f"O maior valor da linha {linha} eh {maiorLinhaX(matriz, linha)}")
