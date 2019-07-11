anime = "Shingeki no Kyojin"
a = anime[4]
b = anime[4:10]
c = anime[2:]
d = anime[3:12:2]
e = anime[:10]
f = anime[2::4]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


contadorA = anime.count('i')
contadorB = anime.count('i', 0, 16)
contadorC = anime.count('i', 5, 16)

print("{} {} {}".format(contadorA, contadorB, contadorC))


procuraA = anime.find("jin")
procuraB = anime.find("Eren")
procuraC = "Shin" in anime #operador in


digimonI = "Digimon Adventure"
digimonIV = digimonI.replace("Adventure", "Frontier")

print(digimonI, digimonIV, sep="\n")


sao = "sword art online"
saoup = sao.upper()
saocap = sao.capitalize()
saotitle = sao.title()

print(sao, saoup, saocap, saotitle, sep=" ---> ", end="\n")


dbz = "    Dragon Ball Z   "
newdbz = dbz.strip()
newdbzr = dbz.rstrip()
newdbzl = dbz.lstrip()



#Divisao
coelhinha = "Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"
divisao = coelhinha.split()
jucao = "-".join(divisao)
print(divisao)
print(jucao)