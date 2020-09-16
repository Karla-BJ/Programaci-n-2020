#Entradas#
listaPesos =[20000,30000,4000,2500,1000,7600]

#-----Preguntas-----#

preguntaEliminarLista='''
Para eliminar un valor de la lista, tenga en cuenta que:0 corresponde a 20000
                                                        1 corresponde a 30000
                                                        2 corresponde a 4000
                                                        3 corresponde a 2500
                                                        4 corresponde a 1000
                                                        5 corresponde a 7600
: '''

PreguntaMenu='''
Porfavor ingrese alguna de estas opciones
            1-Para convertir los montos
            2-Para agregar un valor nuevo a la lista de montos
            3-Para ver el monto más alto, es más bajo y su promedio
            4-Para eliminar un valor de la lista 
            5-Para salir del programa
: '''
preguntaConversión='''
Porfavor ingrese alguna de estas opciones
            C- Para ver la lista en pesos
            D-Para convertir los pesos a dólares
            E-Para convertir los pesos a euros
: '''
#-----Mensajes error-----#
MensajeEntradaNoValida1= 'Recuerde ingresar una opción válida C,D,E'
MensajeEntradaNoValida2= 'Recuerde ingresar una opción válida 1,2,3,4,5'
#-----Mensajes informativos-----#
MensajeOpcion= 'Usted escogió la opción {}'
MensajeDeSalida= 'Gracias por utilizar nuestros servicios'
MensajePesos='No es necesaria la conversión, pero se muestra la lista de pesos'

#-----Inicio código-----#

opcion= int(input(PreguntaMenu))

#-----Cálculos preliminares-----#
listaC=listaPesos
listaD= []
listaE= []

#A dolares C*0.00027#
for elemento in listaC:
    dolares= elemento*0.00027
    listaD.append(dolares)
#A euros C*0.00023#
for elemento in listaC:
    euros= elemento*0.00023
    listaE.append(euros)

#-----Calcular Máximo, mínimo y promedio-----#

mayor=max(listaC)
menor= min (listaC)

sumaValores=0
for elemento in listaC:
    sumaValores+= elemento
promedio=round (sumaValores/len(listaC),3)


#-----Menú-----#
while(opcion!=5):
    if (opcion==1):
        print (MensajeOpcion.format(1))
        #Pregunta conversión#
        conversion=input(preguntaConversión)
        if (conversion=='D'):
            print (listaD)
        elif (conversion=='E'):
            print (listaE)
        elif(conversion== 'C'):
            print (MensajePesos)
            print (listaC)
        else:
            print (MensajeEntradaNoValida1)
    elif(opcion==2):
        print(MensajeOpcion.format(2))
        listaC.append(float(input("Ingrese el valor que desea agregar a la lista : ")))
        print (listaC)
    elif (opcion==3):
        print(MensajeOpcion.format(3))
        print('El monto más alto fue', mayor)
        print('El monto más bajo fue', menor)
        print ('El promedio de los valores de la lista de montos es', promedio)
    elif (opcion==4):
        print (MensajeOpcion.format(4))
        print (preguntaEliminarLista)
        listaC.pop  (int(input("Ingrese el número correspondiente al monto a eliminar : ")))
        print (listaC)
    else:
        print (MensajeEntradaNoValida2)


    #-----Entrada de la variable de la opción-----#
    opcion= int(input(PreguntaMenu))


#-----Salida-----#
print(MensajeDeSalida)
















