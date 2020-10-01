import persona as p 
class Estudiante (p.Persona):
    def __init__ (self, nombreIn, pesoIn, idIn, alturaIn, generoIn, carreraIn, semestreIn, universidadIn):
        p.Persona.__init__(self, nombreIn, pesoIn, idIn, alturaIn, generoIn)
        self.carrera= carreraIn
        self.semestre= semestreIn
        self.universidad= universidadIn
    
    def asistir (self,materia) : 
        print (f"hola soy {self.nombre} y estoy muy motivada, pues asistiré a {materia}")

estudianteP=Estudiante ("karla", 43, 1000411461, 1.61, "femenino", "Ingeniería biomédica", 3, "Universidad CES")
estudianteP.asistir("programación")

