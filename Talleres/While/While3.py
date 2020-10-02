print("El juego termina sí y solo sí, el último número entero que ingreses sea menor que el anterior")

#-----Mensajes-----#
PreguntaNúmero1= ("Hola, porfavor ingrese un número entero : ")
PreguntaNúmero2= ("ingrese un número entero mayor que el anterior : ")
MensajeDeContinuación= ("Cumpliste la condición entonces sigues en el juego")
MensajeDeDespedida= ("Hasta luego, gracias por jugar ♥")

NúmeroIngresado1= int(input(PreguntaNúmero1))
NúmeroIngresado2= int(input(PreguntaNúmero2))

while(NúmeroIngresado1<NúmeroIngresado2):
    print(MensajeDeContinuación)
    NúmeroIngresado2=int(input(PreguntaNúmero2))
print("Ingresaste un número menor al anterior, por eso estás fuera")
print(MensajeDeDespedida)
