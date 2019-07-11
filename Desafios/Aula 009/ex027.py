def FLnome(string):
    #Primeiro e ultimo nome
    divisao = string.split()
    print("Primeiro nome: {}\nUltimo nome: {}".format(divisao[0], divisao[len(divisao)-1]))


nome = str(input("Digite seu nome completo: ")).strip()
FLnome(nome)