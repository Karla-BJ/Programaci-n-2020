print("Hola, bienvenido a la plataforma preventiva de avianca para covid-19. Es un gusto tenerlo como pasajero")

Procedencia=input("Para comenzar, Ingrese su lugar de origen : ")

if(Procedencia== "China" or Procedencia== "Irán" or Procedencia== "Italia"):
    print("Según las disposiciones a partir de la emergencia sanitaria, usted se encuentra en estado de observación")
    print("Gracias por la información")

else:
    Temperatura=float(input("Para continuar con el proceso, porfavor ingrese su temperatura actual : "))
    if(Temperatura<36):
        print("A partir de su temperatura, se encuentra en estado de hipotermia")
        print("Gracias por utilizar nuestros servicios")
    elif(Temperatura>=36 and Temperatura<38.5):
        print("Gracias por utilizar nuestros servicios")
        print("A partir de su temperatura, se encuentra en estado saludable")
    elif(Temperatura>=38.5 and Temperatura<41):
        print("Gracias por utilizar nuestros servicios")
        print("A partir de su temperatura, se encuentra en estado de alerta")
    else:
        print("A partir de su temperatura, se encuentra en estado de peligro")
        print("Gracias por utilizar nuestros servicios")



