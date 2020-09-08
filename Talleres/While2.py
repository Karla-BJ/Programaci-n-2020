print (" Hola, a continuación se le pedirá que ingrese dos números enteros")
#-----Mensajes-----#
PreguntaNúmero1= ("Ingrese el primero : ")
PreguntaNúmero2= ("Ingrese el segundo : ")
MensajeDeDespedida= ("Hasta luego, gracias por jugar ♥")
MensajeRepetición= "Debes ingresar un número mayor al primero"

NúmeroIngresado1= int(input(PreguntaNúmero1))
NúmeroIngresado2= int(input(PreguntaNúmero2))
while(NúmeroIngresado2<NúmeroIngresado1):
    print(MensajeRepetición)
    NúmeroIngresado2= int(input(PreguntaNúmero2))

print(MensajeDeDespedida)

