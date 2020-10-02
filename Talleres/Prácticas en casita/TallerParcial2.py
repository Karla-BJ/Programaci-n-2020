def pares (lista):
    listaPares= []

    for n in lista:
        if n%2==0:
            listaPares.append(n)
    return listaPares

listaNumeros= [10,11,12,13,14,15,16,17,18,19,20]
resultado= pares(listaNumeros)
print(resultado)