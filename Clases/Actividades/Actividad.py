#=========Preguntas========#
Pregunta1= "Ingrese una vocal : "
#=========Mensajes========#
MensajeFallido= "Fallastee, no es la vocal secreta"
MensajeExitoso= "Excelenteee, adivinaste la vocal secreta"
MensajeDerrota= "Lo siento, game over"
MensajeDeDespedida= "Gracias por jugar, nos vemos ♥"
MensajeVidas= ("Ten cuidado, has perdido{} vida/s, Te queda/n {}")

#Ciclos While

VocalSecreta= "A"
VocalIngresada= input(Pregunta1)
VidasPerdidas=0
while(VocalSecreta!=VocalIngresada and VidasPerdidas<=3):
    VidasPerdidas=VidasPerdidas+1
    print(MensajeVidas.Format(VidasPerdidas,3-VidasPerdidas))
    print(MensajeDerrota)
if VidasPerdidas<3:
    VocalIngresada=input(Pregunta1)

if VidasPerdidas<3:
    print(MensajeExitoso)
else:
    print(MensajeDeDespedida)