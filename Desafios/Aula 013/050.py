"""
050
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares
"""
soma = 0
for i in range(6):
    x = int(input("Digite o numero {}: ".format(i+1)))
    if not x % 2:
        soma += x
print("Soma {}".format(soma))