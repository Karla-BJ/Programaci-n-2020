#-----ENTRADAS-----#
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#-----Preguntas-----#
PreguntaMenu='''
Porfavor ingrese alguna de estas opciones
            1- Para convertir temperaturas
            2-Para estado de salud de c/u de las temperaturas
            3-Para ver máximo y mínimo de temperaturas
            4-Para salir del programa
: '''
preguntaConversión='''
Porfavor ingrese alguna de estas opciones
            F- Para convertir temperaturas Farenheit
            K-Para convertir temperaturas Kelvin
            C-Para convertir temperaturas Celcius
'''
#-----Mensajes error-----#
MensajeEntradaNoValidaN= 'Recuerde ingresar una opción válida 1,2,3,4'
MensajeEntradaNoValidaT= 'Recuerde ingresar una opción válida F,C,K'
#-----Mensajes informativos-----#
MensajeOpcion= 'Usted escogió la opción {}'
MensajeDeSalida= 'Gracias por utilizar nuestros servicios'
MensajeCelcius='No es necesaria la conversión, pero se muestra la lista'


#-----Inicio código-----#

opcion= int(input(PreguntaMenu))

#-----Cálculos preliminares-----#
listaK=[]
listaF= []
listaC= Temperatura_Corporal
listaEstadosSalud=[]

#A kelvin 1C+273.15#
for elemento in listaC:
    kelvin= elemento + 273.15
    listaK.append(kelvin)
#A fahrenheit (1C*1.8)+32#
for elemento in listaC:
    Fahrenheit= (elemento*1.8)+32
    listaF.append(Fahrenheit)
#--Detección estados de salud--#
for elemento in listaC:
    estado=''
    if elemento<36:
        estado= 'Hipotermia'
    elif (elemento>= 36 and elemento < 37.6 ):
        estado='normal'
    else:
        estado='Fiebre'
    listaEstadosSalud.append(estado)
#-----Calcular Máximo y mínimo-----#

mayor=max(listaC)
menor= min (listaC)
frecuencia=round (len (listaC)/24,2)


#-----Menú-----#
while(opcion!=4):
    if (opcion==1):
        print (MensajeOpcion.format(1))
        #Pregunta conversión#
        conversion=input(preguntaConversión)
        if (conversion=='K'):
            print (listaK)
        elif (conversion=='F'):
            print (listaF)
        elif(conversion== 'C'):
            print (MensajeCelcius)
            print (listaC)
        else:
            print (MensajeEntradaNoValidaT)
    elif(opcion==2):
        print(MensajeOpcion.format(2))
        print (listaEstadosSalud)
    elif (opcion==3):
        print(MensajeOpcion.format(3))
        print('La temperatura máxima fue', mayor)
        print('La temperatura mínima fue', menor)
        print ('La temperatura fue tomada con una frecuencia de', frecuencia)
    else:
        print (MensajeEntradaNoValidaN)


    #-----Entrada de la variable de la opción-----#
    opcion= int(input(PreguntaMenu))


#-----Salida-----#
print(MensajeDeSalida)
