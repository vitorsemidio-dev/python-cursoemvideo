def precoTotal(km, dias):
    precoPorKm = 0.15
    precoPorDia = 60.00
    total = km * precoPorKm + dias * precoPorDia
    return total

dias = int(input("Informe quantos dias ficou com o veiculo: "))
km = float(input("Informe quantos km andou com o carro: "))

total = precoTotal(km, dias)
print("O preco total a pagar por usar o carro por {} dias e ter precorrido {:.1f} km sera {:.2f}".format(dias, km, total))



