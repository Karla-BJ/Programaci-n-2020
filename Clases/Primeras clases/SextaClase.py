#----Se crea la listaNombres----
listaNombres=[]
listaNombres=["Melany",
        "Karla",
        "Laura P",
        "Laura M",
        "Juan Pablo",
        "Mario",
        "Santiago"]

listaEdades= [20,18,18,18,21,20,18,18]
print(listaNombres)
print (listaNombres[1])
print (listaNombres[-1])
listaNombres.append("daniel")
listaEdades.append(27)

listaNombres.pop(3)
print(listaNombres)
listaNombres.append("Laura M")

sizelist= len(listaNombres)
print (sizelist)

for i in range (sizelist):
    print (f"hola soy {listaNombres [i]} y estoy feliz programando")
print("segundo método")
for nombre in listaNombres:
    print (f"hola soy {nombre} y estoy feliz programando")


for i in range (sizelist):
    print (f"nombre: {listaNombres [i]} Edad: {listaEdades[i]}")

listaHobbies= []
decision= "si"
while(decision=="si"):
    Hobbie=input("¿Cuál es tu hobbie favorito?")
    listaHobbies.append(Hobbie)
    decision= int(input("""ingrese : 
            Si= Para seguir agregando hobbies
            No= Para finalizar
    :"""))
print (listaHobbies)

