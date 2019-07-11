def indice(procura, tupla):
    for pos, item in enumerate(tupla):
        if procura == item:
            return pos
    return -1

numeros = [1,2,5,8]
linguagem = ("C++", "C", "Python", "C#", "HTML", "JavaScript", "Java", "CSS", "VBA", "Haskell", "Kotlin")
web = ("JavaScript", "HTML", "CSS", "PHP")
del(web)
"""
for pos, ling in enumerate(linguagem):
    print(f"Posicao {pos}: {ling}")
"""
print(sorted(linguagem))

#x = linguagem.index("CCC")

if indice("C++", linguagem) >= 0:
    print("Existe")
else:
    print("Nao existe!")
#print("{}".format(linguagem.index("CSS")))
