import persona as p 
import estudiante as es 
class Egresado (es.Estudiante):
    def __init__ (self, nombreIn, edadIn, idIn, carreraIn, fechaIn):
        es.Estudiante.__init__(self,nombreIn,edadIn,idIn,carreraIn,"egresado")
        self.fecha= fechaIn
    def trabajar (self,empresa):
        print (f"hola, soy {self.nombre} y trabajo en la empresa {empresa}")