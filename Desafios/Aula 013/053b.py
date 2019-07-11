frase  = str(input("Digite aqui uma frase:")).lower().replace(" ", "")
if frase == frase[::-1]:
    print(" {} é um palíndromo".format(frase))
else:
    print(" {} Não é um palíndromo".format(frase))