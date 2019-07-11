def maior(a, b):
    if a > b:
        print("O primeiro valor eh maior")
    elif b > a:
        print("O segundo valor eh maior")
    else:
        print("Nao exite valor maior. Ambos são iguais")

n = input("Digite dois numeros: ")
divisao = n.split(" ")
primeiro = int(divisao[0])
segundo = int(divisao[1])

maior(primeiro, segundo)

