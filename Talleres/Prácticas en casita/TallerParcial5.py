class Paciente ():
    def __init__ (self, idIn, nombreIn, generoIn, afiliadoIn):
        self.id= idIn
        self.nombre= nombreIn
        self.genero= generoIn
        self.afiliado= afiliadoIn
    def atributos (self):
        print (f"El/La paciente llamado {self.nombre} de género {self.genero}, está identificado con una cc {self.id}  y está afiliado/a a {self.afiliado}")
    def sintomas (lista):
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


class Estable (Paciente):
    def __init__ (self, idIn, nombreIn, generoIn, afiliadoIn, tiempoIn, temperaturaIn, animoIn ):
        Paciente.__init__(self, idIn, nombreIn, generoIn, afiliadoIn)
        self.tiempo= tiempoIn
        self.temperatura= temperaturaIn
        self.animo= animoIn
    def atributos2 (self):
        print (f"El/La paciente llamado {self.nombre} de género {self.genero}, está identificado con una cc {self.id}  y está afiliado/a a {self.afiliado}; tuvo un tiempo de espera de {self.tiempo}, una temperatura de {self.temperatura} y se encuentra {self.animo}")
    def compromiso (self):
        recomendaciones= ["cuidarse del frío", "tomar ibuprofeno cada 12 horas", "y ponerse paños de agua fría para la fiebre"]
        print (f"El/La paciente {self.nombre} se compromete a cumplir con las recomendaciones del profesional en salud, las cuales son : ") 
        print(recomendaciones[0]) 
        print (recomendaciones[1])
        print (recomendaciones[2])


class Crítico (Paciente):
    def __init__(self, idIn, nombreIn, generoIn, afiliadoIn, numeroHabIn, patologiaIn):
        Paciente.__init__(self, idIn, nombreIn, generoIn, afiliadoIn)
        self.habitacion= numeroHabIn
        self.patologia= patologiaIn
    def atributos3 (self):
        print (f"El/La paciente llamado {self.nombre} de género {self.genero}, está identificado con una cc {self.id}, está afiliado/a a {self.afiliado} y se encuentra en la habitación {self.habitacion}. El motivo de hospitalización es por {self.patologia}")
    def sintomas2 (lista2):
        decision= "si"
        listaSintomas2= []
        while(decision=="si"):
            listaSintomas2= []
            sintomasIn2=input(f"¿Cuáles síntomas presenta el paciente? : ")
            listaSintomas2.append(sintomasIn2)
            decision= (input("""ingrese : 
                    si= Para seguir agregando síntomas
                    No= Para finalizar
            :"""))
        print (f"La lista de síntomas del paciente es:")
        print (listaSintomas2)


jaime= Paciente (1000588963, "Jaime", "masculino", "Sura")
jaime.atributos()
jaime.sintomas()
karen= Estable (1000548612, "Karen", "femenino", "Colsanitas", "30 minutos", 36, "un poco decaida")
karen.atributos2()
karen.compromiso ()
karla= Crítico (1000411461, "Karla", "femenino", "Pablo Tobón Uribe", 17, "Coronavirus")
karla.atributos3 ()
karla.sintomas2 ()