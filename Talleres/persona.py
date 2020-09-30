class Persona():
    #creación#
    def __init__ (self, nombreIn, pesoIn, idIn, alturaIn, generoIn):
        self.nombre= nombreIn
        self.peso= pesoIn
        self.id= idIn
        self.altura= alturaIn
        self.genero= generoIn
        print ("se creó una persona")
    def atributos (self):
        print (f"hola, mi nombre es {self.nombre}, mi género es {self.genero} tengo {self.edad} años, peso {self.peso} kg, mido {self.estatura} m y mi id es {self.id}")

karla=("karla", 43, 1000411461, 1.61, "femenino")