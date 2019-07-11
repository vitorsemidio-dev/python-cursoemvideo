def paridade(numero):
    return (numero % 2) == 0


numero = int(input("Digite um numero: "))
if paridade(numero):
    print("O numero digitado eh par")
else:
    print("O numero digitado eh impar")