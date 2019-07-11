def toBinario(num):
    return str(bin(num))[2:]
def toOctal(num):
    return str(oct(num))[2:]
def toHexa(num):
    return str(hex(num))[2:]


num = int(input("Digite um numero inteiro: "))

print("Escolhe uma opção: ")
print("[ 1 ] converter para BINARIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opcao = int(input("Sua opção: "))

if opcao == 1:
    binario = toBinario(num)
    print("{} convertido para binario eh igual a: {}".format(num, binario))
elif opcao == 2:
    octal = toOctal(num)
    print("{} convertido para octal eh igual a: {}".format(num, octal))
else:
    hexa = toHexa(num)
    print("{} convertido para hexadecimal eh igual a: {}".format(num, hexa))

