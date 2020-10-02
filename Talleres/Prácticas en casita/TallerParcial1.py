print ("segundo punto")

def infolista (lista):
    mayor= max (lista)
    menor= min (lista)

    acumulador=0
    for elemento in lista:
        acumulador += elemento
    sizeList= len (lista)
    promedio= acumulador/sizeList
    print (f"El número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}")

Tallas= [36,38,42,35,37,45,28,39,41,40]
infolista(Tallas)
