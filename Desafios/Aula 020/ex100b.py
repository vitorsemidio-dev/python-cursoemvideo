def soma_lista(lista):
    
    if lista[0] % 2:
        if len(lista) == 1:
            return 0
        return soma_lista(lista[1:])

    if len(lista) == 1:
        return lista[0]

    return lista[0] + soma_lista(lista[1:])

lista = [1,5,2,8,61,21]
soma = soma_lista(lista)
print(soma)