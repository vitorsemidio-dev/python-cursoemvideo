text = {
    "fecha":"\033[m",
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m"
}

def situacao(media):
    if media >= 7:
        return 1
    elif media >= 5:
        return 0
    return -1

notas = input("Informe suas duas notas: ")
divisao = notas.split(" ")
notaA = float(divisao[0])
notaB = float(divisao[1])

media = (notaA + notaB) / 2

if situacao(media) == 1:
    print("{}Aprovado".format(text["verde"]))
elif not situacao(media):
    print("{}Prova de Recuperação".format(text["amarelo"]))
else:
    print("{}Reprovado".format(text["vermelho"]))