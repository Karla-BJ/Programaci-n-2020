import persona as p 
import estudiante as es
import egresado as eg 
laura= p.Persona("laura", 18, 28137231)
mario= p.Persona("laura", 20, 21442214)
valeria= es.Estudiante ("Valeria",18,215346,"biomédica",3)
melany= eg.Egresado ("Melany",18,143413,"biomédica",12/2030")
print (melany.semestre)
laura.hablar("Todo anda muy bien, me gusta aprender ♥")
mario.comer("taco")
valeria.estudiar ("cálculo")  
melany.trabajar("MIT")