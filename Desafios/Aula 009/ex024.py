def comecaCom(ref, string):
    if string.split()[0][:len(ref)] == ref.lower():
        return True
    return False


cidade = str(input("Informe o nome de uma cidade: ")).lower().strip()
comparacao = "santo"

if comecaCom(comparacao, cidade):
    print("A cidade {} começa com {}".format(cidade.title(), comparacao.capitalize()))
else:
    print("A cidade {} não começa com {}".format(cidade.title(), comparacao.capitalize()))