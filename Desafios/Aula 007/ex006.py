#dobro, triplo e raiz quadrada

numero = int(input("Informe um numero: "))

dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)

print("Dobro {:>5}".format(dobro))
print("Triplo {:>5}".format(triplo))
print("Raiz {0:>9.3f}".format(raiz))