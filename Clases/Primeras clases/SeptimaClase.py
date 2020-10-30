import random

MensajeFallido=("Lo siento, vuelve a intentarlo")
PreguntaNúmero= ("Porfavor ingresa un número para adivinar lo que sale del dado : ")
MensajeExitoso=("Lo lograste")
MensajeDeDespedida= ("Gracias por jugar, nos vemos ♥")

Dado= random.randint (1,6)

Persona= int(input(PreguntaNúmero))
while(Dado!=Persona):
    print(MensajeFallido)
    Persona=int(input(PreguntaNúmero))
print(Dado)
print(MensajeExitoso)
print(MensajeDeDespedida)



