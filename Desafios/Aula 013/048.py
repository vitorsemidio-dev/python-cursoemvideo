"""
048
Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de três entre 1 e 500
"""

def somaPA(inicio, fim, passo):
    if inicio % passo != 0:
        primeiro = inicio + passo - (inicio%passo)
    else:
        primeiro = inicio
    passo += 3
    ultimo = fim - (fim%passo)
    qtdTermos = int ((ultimo - primeiro) / passo +1)
    print("Primeiro: {}\nUltimo: {}\nQuantidade de Termos: {}".format(primeiro, ultimo, qtdTermos))
    for i in range(primeiro, ultimo, passo):
        print("{}".format(i), end=" ")
    result = qtdTermos * (primeiro+ultimo) /2
    print("\nResultado: {}".format(result))
    return result

inicio = 1
fim = 16
passo = 3

somaPA(inicio, fim, passo)

"""
soma = 0
for i in range(inicio, fim+1, passo):
    if i % 2 != 0:
        print("{}".format(i), end=" ")

print("Soma: {}".format(soma))
"""