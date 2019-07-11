def celToF(celsius):
    return celsius*(5/9)+32


celsius = float(input("Informe a temperatura em Cº: "))
fahr = celToF(celsius)
print("A temperatura de {:.1f} Cº corresponde a {:.1f}Fº!".format(celsius, fahr))