def calcularValor(distancia, preco):
    return distancia*preco


distancia = int(input("Digite a distancia entre as cidades: "))
limite = 200
if distancia <= limite:
    print("Viagem ateh de 200km")
    print("Preco a pagar por uma viagem de {} km sera R${:.2f}".format(distancia, calcularValor(distancia, 0.50)))
else:
    print("Viagem acima de 200km")
    print("Preco a pagar por uma viagem de {} km sera R${:.2f}".format(distancia, calcularValor(distancia, 0.45)))