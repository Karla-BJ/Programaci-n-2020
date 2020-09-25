class Persona:
    def __init__ (self, estaturaIngresado, pesoIngresado, nombreIngresado, idIngresado, EdadIngresada):
        self.raza= "humano"
        self.estatura= estaturaIngresado
        self.edad= EdadIngresada
        self.nombre= nombreIngresado
        self.peso= pesoIngresado
        self.id= idIngresado
        print ("Hola mundo estoy viv@ ♥")
    def caminar (self):
        print ("Hola voy a caminar")
    def saludo (self, saludoEspecial):
        print (saludoEspecial)
class Arquitecta (Persona):
    def dibujarPlanos (self):
        print (f"hola soy {self.nombre} y voy a dibujar el plano")
class Biomedico (Persona):
    def cultivarCelulas (self):
        print (f"hola soy {self.nombre} y voy a cultivar células")

karla= Arquitecta (1.61,43,"Karla",1000411461,18)
karla.caminar ()
juan= Biomedico (1.76,82,"Juan Pablo",1006723451,23)
juan.caminar ()
karla.saludo ("Holi crayoli")
juan.saludo ("Hola coca-cola")
karla.dibujarPlanos()
juan.cultivarCelulas ()