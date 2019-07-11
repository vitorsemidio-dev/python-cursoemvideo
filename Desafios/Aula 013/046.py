"""
046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
Indo de 10 ateh 0, com uma pausa de 1 segundo entre elas.
"""

from time import sleep

for i in range(11, 0, -1):
    print("{}".format(i-1))
    sleep(1)
