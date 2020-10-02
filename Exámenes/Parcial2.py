print("punto 1")
numeroIn=(int(input("Hola, ingresa un número entero para elevarlo al cuadrado :")))
def cuadrado (numero):
    return numero**2
    operación= numeroIn**2



print("punto 2")
numeroIn=(int(input("Hola, ingresa un número entero para elevarlo al cubo :")))
def cubo (numero):
    return numero**3
    operación= numeroIn**3



print("punto 3")
numeroIn=(int(input("Hola, ingresa un número entero para elevarlo a la cuatro :")))
def cuatro (numero):
    return numero**4
    operación= numeroIn**4



print("punto 4")
numeroIn=(int(input("Hola, ingresa un número entero para elevarlo a la cinco :")))
def cinco (numero):
    return numero**5
    operación= numeroIn**5



print("punto 5")
def calculadora (accion,valor):
    print (accion(valor))
calculadora (cuadrado, numeroIn)
calculadora (cubo, numeroIn)
calculadora (cuatro, numeroIn)
calculadora (cinco, numeroIn)

print("punto 6")

class Doctor ():
    def __init__(self, idIn, nombreIn, generoIn, universidadIn):
        self.id= idIn
        self.nombre= nombreIn
        self.genero= generoIn
        self.universidad= universidadIn
    def atributos (self):
        print (f"Hola, mi nombre es {self.nombre}, estoy identificado/a con cc {self.id}, de género {self.genero} y soy egresado/a de la universidad {self.universidad} ")
    def sintomas1 (lista):
        decision= "si"
        listaSintomas= []
        while(decision=="si"):
            sintomasIn=input(f"¿Cuáles síntomas presenta el paciente? : ")
            listaSintomas.append(sintomasIn)
            decision= (input("""ingrese : 
                    si= Para seguir agregando síntomas
                    No= Para finalizar
            :"""))
        print (f"La lista de síntomas del paciente es:")
        print (listaSintomas)

class Neurologo (Doctor):
    def __init__(self, idIn, nombreIn, generoIn, universidadIn, experienciaIn, consultorioIn, salarioIn):
        Doctor.__init__ (self, idIn, nombreIn, generoIn, universidadIn)
        self.experiencia= experienciaIn
        self.consultorio= consultorioIn
        self.salario= salarioIn
    def atributos2 (self):
        print  (f"Hola, mi nombre es {self.nombre}, estoy identificado/a con cc {self.id}, de género {self.genero} y soy egresado/a de la universidad {self.universidad}. LLevo {self.experiencia} de experiencia en el área de la salud, trabajo en el consultorio número {self.consultorio} y mi salario aproximado es de {self.salario} ")
    def pacientes (self):
        decision= "si"
        while(decision=="si"):
            listaPacientes= []
            pacientesIn=input("Ingrese los nombres de los pacientes : ")
            listaPacientes.append(pacientesIn)
            decision= (input("""ingrese : 
                    si= Para seguir agregando pacientes
                    No= Para finalizar
            :"""))
            for elemento in (listaPacientes):
                print (f"Antenderé al paciente {elemento}")



class Cardiologo (Doctor):
    def __init__(self, idIn, nombreIn, generoIn, universidadIn, experienciaIn, consultorioIn, salarioIn):
        Doctor.__init__ (self, idIn, nombreIn, generoIn, universidadIn)
        self.experiencia= experienciaIn
        self.consultorio= consultorioIn
        self.salario= salarioIn
    def atributos3 (self):
        print  (f"Hola, mi nombre es {self.nombre}, estoy identificado/a con cc {self.id}, de género {self.genero} y soy egresado/a de la universidad {self.universidad}. LLevo {self.experiencia} de experiencia en el área de la salud, trabajo en el consultorio número {self.consultorio} y mi salario aproximado es de {self.salario} ")
    def sintomas2 (lista):
        decision= "si"
        listaSintomas= []
        while(decision=="si"):
            sintomasIn=input(f"¿Cuáles síntomas presenta el paciente? : ")
            listaSintomas.append(sintomasIn)
            decision= (input("""ingrese : 
                    si= Para seguir agregando síntomas
                    No= Para finalizar
            :"""))
        print (f"La lista de síntomas del paciente es:")
        print (listaSintomas)
        print ("Ya se que tiene este paciente")

celeste= Doctor (1000411461, "Celeste", "femenino", "CES")
celeste.atributos()
celeste.sintomas1()
pablo= Neurologo (1452348951, "Pablo", "masculino", "de Antioquia", " 5 años", 1775, " 15 millones")
pablo.atributos2 ()
pablo.pacientes ()
mateo= Cardiologo (5489123601, "Mateo", "masculino", "de los Andes", "10 años", 1296, "20 millones")
mateo.atributos3 ()
mateo.sintomas2 ()


