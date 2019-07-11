def calcularMulta(vel, limite, custo):
    multa = (vel - limite) * custo
    return multa

velocidade = int(input("Digite a velocidade do carro: "))
limite = 80
custo = 7.00
if velocidade > 80:
    print("Acima do limite de velocidade.")
    print("Carro multado e o valor da multa sera: R${:.2f}".format(calcularMulta(velocidade, limite, custo)))
else:
    print("Carro abaixo da velocidade maxima")
