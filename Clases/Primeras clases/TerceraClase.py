a=int(input("Ingrese el primer número entero : "))
b=int(input("Ingrese el segundo número entero : "))
print (a,b)

if (a==b):
    print("son números iguales")
elif(a>b):
    print(f"El número {a} es mayor que {b}")
else:
    print(f"el número {b} es mayor que {a}")

    #Dada una temperatura, determinar si el paciente está sano no 
    #Temperatura menor a 36 grados: hipotermia
    #Temperatura en el intervalo de 36-38 grados: normal
    #Temperatura en el intervalo de 37.5-38 grados: normal
    #Temperatura mayor a 38 grados: fiebre
    #Muestre el nombre del paciente y su estado

nombre=input("ingrese el nombre del paciente : ")
temperatura= float (input("ingrese la temperatura del paciente : "))
if (temperatura<36) : 
    print(f"El paciente llamado {nombre} se encuentra en estado de hipotermia")
elif(temperatura>=36 and temperatura<37.5) : 
    print(f"El paciente llamado {nombre} se encuentra en estado normal")
elif(temperatura>=37.5 and temperatura<38):
    print(f"El paciente llamado {nombre} se encuentra en estado de alerta")
else:
    print(f"El paciente llamado {nombre} se encuentra con fiebre")



