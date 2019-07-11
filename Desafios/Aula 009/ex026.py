"""
026
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""
def conta(ref, frase):
    return frase.lower().count(ref.lower())

def primeraOcorrencia(ref,frase):
    return frase.lower().find(ref)

def ultimaOcorrencia(ref, frase):
    x = -1
    for i in range(len(frase)):
        if frase[i].lower() == ref:
            x = i
    return x

frase = str(input("Digite uma frase: ")).strip()
ref = "a"

contador = conta(ref, frase)
print("A frase possui {} letra(s) {}".format(contador, ref))

ocorrencia = primeraOcorrencia(ref, frase)
ultima = ultimaOcorrencia(ref, frase)
if (ocorrencia >= 0):
    print("A primeira ocorrência da letra {} foi na posicao {}".format(ref, ocorrencia+1))
    print("A ultima ocorrência da letra {} foi na posicao {}".format(ref, ultima + 1))
else:
    print("A letra {} nao aparece na frase \"{}\"".format(ref, frase))
