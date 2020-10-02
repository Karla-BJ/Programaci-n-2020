#-----Mensajes-----#
PreguntaNúmero= ("Hola, porfavor ingrese un número entero para continuar; Si desea finalizar, escriba 0 : ")
MensajeFinal= ("Has decidido parar el conteo")
MensajeDeDespedida= ("Hasta luego, gracias por jugar ♥")

Suma=0
NúmeroFinalizar= 0
NúmeroIngresado= int(input(PreguntaNúmero))
while(NúmeroFinalizar!=NúmeroIngresado):
    Suma+= NúmeroIngresado
    NúmeroIngresado=int(input(PreguntaNúmero))
print(MensajeFinal)
print (Suma)
print(MensajeDeDespedida)
