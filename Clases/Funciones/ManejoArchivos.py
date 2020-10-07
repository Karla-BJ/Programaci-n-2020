#Leer

archivo = open ("Poema.txt", encoding= "UTF-8")
print (archivo)
lines=archivo.readlines()
archivo.close()
print (lines)
listaRenglones=[]
with open ("Poema.txt", encoding= "UTF-8") as lines:
    for line in lines:
        print (line)
        listaRenglones.append (line)

print (listaRenglones)

nombre= input ("ingrese su nombre : ")
edad = int (input("ingrese su edad : "))
opinion = input ("ingrese su opinión : \n")

archivo = open ("opinion.txt","w", encoding= "UTF-8")
archivo.write (f"opinión de {nombre}")
archivo.write (f"Edad : {edad} \n")
archivo.write (f"Reseña : {opinion} \n")
archivo.close ()