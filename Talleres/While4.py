print("Bienvenido al servicio de compras digitales, para saber cuánto es el valor a pagar, ingresa el precio de cada producto que desee")
print("Al momento de finalizar el ingreso de datos, digitar 0")
#-----Mensajes-----#
PreguntaPrecio= ("porfavor ingrese el precio del producto: $ ")
MensajeDeContinuación= ("ingresaste el número 0, por ende damos por hecho que tu lista de productos está completa")
MensajeDeDespedida= ("Hasta luego, gracias por usar nuestros servicios")

Suma=0

PrecioIngresado= float(input(PreguntaPrecio))
while PrecioIngresado!=0:
    if PrecioIngresado<0:
        print("Ingrese un precio válido")
    else:
        Suma+=PrecioIngresado
    PrecioIngresado=float(input(PreguntaPrecio))
if (Suma>1000):
    Suma-=Suma*0.1
print(f"El total a pagar por sus productos es de $ {Suma}" )
print(MensajeDeDespedida)

