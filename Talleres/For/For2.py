#-----Mensajes-----#
PreguntaNúmero= ("Hola, porfavor ingrese un número entero para dar a conocer su factorial: ")
MensajeDeDespedida= ("Hasta luego, gracias por jugar ♥")

Factorial= 1
NúmeroIngresado= int(input(PreguntaNúmero))
for i in range (NúmeroIngresado):
    Factorial=Factorial*(i+1)
print(f"El factorial del número entero previamente ingresado, es {Factorial}")