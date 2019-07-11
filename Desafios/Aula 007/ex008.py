#Ler metros e passar para cm e mm

def metrosTocm(metros):
    return metros*100

def metrosTomm(metros):
    return metros*1000


metros = float(input("Digite o valor em metros: "))

cm = metrosTocm(metros)
mm = metrosTomm(metros)

print("{:.2f} equivale a {:.0f} cm e {:.0f} mm".format(metros, cm, mm))

