idadeAlistamento = 18
def alistamento(idade):
    if idade == idadeAlistamento:
        print("{}Coitado! Hora de se alistar{}".format("\033[31m", "\033[m"))
    elif idade > idadeAlistamento:
        print("{}Ufa! Já passou a epoca do alistamento{}".format("\033[34m", "\033[m"))
        print("Passaram {} anos".format(idade-idadeAlistamento))
    else:
        print("{}A sua hora de capinar ira chegar{}".format("\033[33m", "\033[m"))
        print("Faltam {} anos".format(idadeAlistamento-idade))

from datetime import date

anoNascimento = int(input("Digite o seu ano de nascimento: "))
idade = date.today().year - anoNascimento

alistamento(idade)