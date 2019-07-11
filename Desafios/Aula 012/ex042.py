def triangulo(a, b, c):
    if a*b*c <= 0:
        return False
    if a <= abs(b - c) or a > (b+c):
        return False
    return True

def tipoTriangulo(a, b, c):
    if a == b and b == c:
        return 0
    if a == b or a == c or b == c:
        return 1
    return 2

tipos = ["Equilatero", "Isosceles", "Escaleno"]

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if triangulo(a, b, c):
    print("Forma um triangulo do tipo {}".format(tipos[tipoTriangulo(a, b, c)]))
else:
    print("{}Nao forma triangulo{}".format("\033[31m", "\033[m"))