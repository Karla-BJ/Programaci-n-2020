#----mensaje---#
preguntaNumero= (" Porfavor ingrese un número entero : ")

sumaNegativos=0
promedioPositivos=0
sumaPositivos=0
contadorPositivos=0

for i in range (6):
    numeroIngresado= int(input(preguntaNumero))
    if (numeroIngresado<0):
        sumaNegativos+=numeroIngresado
    elif (numeroIngresado>0):
        contadorPositivos+=1
        sumaPositivos+=numeroIngresado


if (contadorPositivos>0):
    promedioPositivos= sumaPositivos/contadorPositivos
    print(f"El promedio de los números positivos es igual a {promedioPositivos}")

else:
    print("No hay números positivos, por ende no es posible dividir por 0")

print(f"La suma de los números negativos es igual a {sumaNegativos}")



