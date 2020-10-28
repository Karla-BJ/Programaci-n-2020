#Primer punto#
archivo1= open ("parrafo.txt", "w")

#Segundo punto#
archivo1= open ("parrafo.txt", "w", encoding  = 'UTF-8')
archivo1 .write ("Programación es el proceso de tomar un algoritmo \n y codificarlo en una notación, un lenguaje de programación, \n de modo que pueda ser ejecutado por una computadora.\n Aunque existen muchos lenguajes de programación y muchos tipos diferentes de computadoras, \n el primer paso es la necesidad de tener una solución.")
archivo1.close ()

#Tercer punto#
listaRenglones=[]
with open ("parrafo.txt", encoding= "UTF-8") as lines:
    for line in lines:
        print (line)
        listaRenglones.append (line)

print ("Trabajé en equipo con Laura Montoya ♥")