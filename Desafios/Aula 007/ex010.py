#Converter real para dolar. Adotando US$1,00 = R$3,27
cotacaoDolar = 3.27
def realToDolar(real):
    return real/cotacaoDolar

real = float(input("Digite quantos reais possui: "))

dolar = realToDolar(real)

print("Com R${:.2f} eh possui comprar US${:.2f}".format(real, dolar))