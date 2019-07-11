#area da parede e qtd de tinta
litroTinta = 2.0

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura*altura

totalTinta = area/litroTinta

print("Para pintar uma parede de area {:.2f} serao necessarios {:.2f} L de tinta".format(area, totalTinta))