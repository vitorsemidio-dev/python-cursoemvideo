import math

real = float(input("Digite um numero real: "))
inteiro1 = int(real)
inteiro2 = math.trunc(real)

print("A parte inteira do numero {} eh {} {}".format(real, inteiro1, inteiro2))