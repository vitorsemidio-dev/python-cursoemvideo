def maiuscula(string):
    print("Nome em maiusculo: {}".format(string.strip().upper()))

def minuscula(string):
    print("Nome em minusculo: {}".format(string.strip().lower()))

def contadorLetras(string):
    print("Quantidade de letras: {}".format(len(string)-string.count(" ")))

def contadorFirst(string):
    print("Quantidade de letras do primeiro nome: {}".format(len(string.split()[0])))

#poderia colocar strip jah na leitura
nome = str(input("Digite seu nome completo: "))
maiuscula(nome)
minuscula(nome)
contadorLetras(nome)
contadorFirst(nome)
texto = "Unidade Dezena Centena Milhar"
print(texto)