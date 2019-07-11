palavras = "Unidade Dezena Centena Milhar"
def matematica(numero):
    for i in range(4):
        print("{}: {}".format(palavras.split()[i], numero%10))
        numero = numero // 10


def texto(string):
    number = string // 1
    matematica(number)


ler = input("Digite um numero de 0 a 9999: ")
num = int(ler)
string = str(ler)

print("Numero")
matematica(num)
print("String")
texto(num)