#A partir de la masa en kg de una persona y su estatura en m, determinar su IMC y en que condición se encuentra
#menor a 18.5= Infrapeso
#De 18.5 a 24.9= Peso normal
#De 25 a 29.9= Sobrepeso
#De 30 a 34.9= Obesidad
#Mayores que 35= Obesidad mórbida

Nombre=input("Porfavor ingrese su nombre : ")
Peso=float(input(f"hola {Nombre}, Para calcular su IMC, comience ingresando su peso actual en Kg : "))
Estatura=float(input("perfecto, ahora ingrese su estatura en m : "))

IMC=round(Peso/Estatura**2)

if(IMC<18.5):
    print(f"{Nombre}, su IMC es de {IMC}. En conclusión, usted se encuentra en estado de infrapeso")
elif(IMC >=18.5 and IMC<25) : 
    print(f"{Nombre}, su IMC es de {IMC}. En conclusión, usted se encuentra en estado saludable con un peso normal")
elif(IMC>=25 and IMC<30) :
    print(f"{Nombre}, su IMC es de {IMC}. En conclusión, usted se encuentra en estado de sobrepeso")
elif(IMC>=30 and IMC<35) :
    print(f"{Nombre}, su IMC es de {IMC}. En conclusión, usted se encuentra en estado de obesidad")
else:
    print(f"{Nombre}, su IMC es de {IMC}. En conclusión, usted se encuentra en estado de obesidad mórbida")

print("Hasta luego, gracias por utilizar nuestro servicio jajaja ♥")




