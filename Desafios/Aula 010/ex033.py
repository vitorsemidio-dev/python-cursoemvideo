def maior(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            print("O maior numero eh: {}".format(n1))
        else:
            print("O maior numero eh: {}".format(n3))
    else:
        if n2 > n3:
            print("O maior numero eh: {}".format(n2))
        else:
            print("O maior numero eh: {}".format(n3))

def menor(n1, n2, n3):
    if n1 < n2:
        if n1 < n3:
            print("O menor numero eh: {}".format(n1))
        else:
            print("O menor numero eh: {}".format(n3))
    else:
        if n2 < n3:
            print("O menor numero eh: {}".format(n2))
        else:
            print("O menor numero eh: {}".format(n3))

numero = [0, 0, 0]
for i in range(len(numero)):
    numero[i] = int(input("Digite o numero {}: ".format(i+1)))

maior(numero[0], numero[1], numero[2])
menor(numero[0], numero[1], numero[2])