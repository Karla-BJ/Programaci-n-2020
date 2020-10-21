import funcionesArchivos as helper
nameFile= "libro.txt"
helper.agregarLinea ("opinion.txt", "nueva linea")
renglonesLibro = helper.leerArchivos (nameFile )

if (len(renglonesLibro)==0):
    print ("Es la primera línea que se escribirá en el libro")
    helper.agregarLinea (nameFile , "El día que programar fue fácil")
else:
    linea= input ("ingrese la línea que desee agregar : \n")
    helper.agregarLinea (nameFile , linea)

