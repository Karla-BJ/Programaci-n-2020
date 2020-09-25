class TortaRedonda: #SIEMPRE CLASES EN MAYUSCULA#
    def __init__ (self,saborIngresado):
        #Definiendo atributos
        self.forma = "Redonda"
        self.sabor = saborIngresado
        #Acción al crear objeto
        print ("Acabo de salir del horno")
    def mostrar_atributos (self):
        print (f"soy de forma {self.forma} y de sabor {self.sabor}")


#Se creó la torta#
tortaChocolate = TortaRedonda ("Chocolate")
tortaVainilla = TortaRedonda ("Vainilla")

#Se muestran atributos#
print (tortaChocolate.sabor)
print (tortaVainilla.sabor)

print (tortaChocolate.forma)
print (tortaVainilla.forma)

#
tortaChocolate.mostrar_atributos()
tortaVainilla.mostrar_atributos()
