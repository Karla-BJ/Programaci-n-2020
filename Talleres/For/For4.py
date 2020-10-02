import random
listaCanciones=["Over the rainbow",
        "Santa Mónica dream",
        "Always",
        "Labios compartidos",
        "Te regalo"]

print("Hola, bienvenido a mi lista de canciones favoritas")
sizelist= len(listaCanciones)

for i in range (sizelist):
    print (f"Este es una de ellas: {listaCanciones [i]}")

print (listaCanciones [random.randint(1,5)])
