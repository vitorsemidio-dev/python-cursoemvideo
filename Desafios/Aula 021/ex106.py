from time import sleep


import abc


def linha(string):
    li = "-"*(len(string)+2)
    print(li)
    print(f" {string}")
    print(li)

def cor(nome):
    print("\033[40m", end="")

while False:
    funcao = str(input("Nome da Funcao: ")).strip().lower()
    if funcao == "fim":
        print("Ateh logo!")
        sleep(1)
        break

    acesso = "Acessando o manual do comando "
    acesso += "\033[45m" + funcao + "\033[m"
    linha(acesso)
    sleep(1)
    cor("Branco")
    help(funcao)
    print("\033[m", end="")








#funcao = str(input("\033[44mDigito o nome da funcao: "))
print("\033[45moi")


#help(abc)