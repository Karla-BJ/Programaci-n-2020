#=========Preguntas========#
PreguntaNúmero= "Ingrese un número del 1 al 10 : "
#=========Mensajes========#
MensajeFallido: "Fallastee, no es el número secreto, me debes una salchipapa"
MensajeExitoso: "Excelenteee, adivinaste el número, te debo una salchipapa"
MensajeDeDespedida: "Gracias por jugar, nos vemos ♥"
#Ciclos While

NúmeroSecreto= 7
NúmeroIngresado= int(input(PreguntaNúmero))
while(NúmeroSecreto!=NúmeroIngresado):
    print(MensajeFallido)
    NúmeroIngresado=int(input(PreguntaNúmero))
print(MensajeExitoso)
print(MensajeDeDespedida)
