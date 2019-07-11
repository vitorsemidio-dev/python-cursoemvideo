#Ler o numero e mostrar a tabuada

n = int(input("Digite um numero: "))

print("A TABUADA DE {}".format(n))
for i in range(1,11):
    print("{} X {:>2}\t= {}".format(n, i, n*i))
