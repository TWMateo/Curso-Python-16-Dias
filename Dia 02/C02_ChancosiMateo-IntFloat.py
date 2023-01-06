from builtins import input
#Los input reciben datos que transforman a string y nada mas si
#se desea que un dato ingresado se transforme a numero se tendra
#que hacer la conversion
mi_numero=1
print("Numero 1: {}".format(mi_numero))
print("Mostrando el tipo de dato: {}".format(type(mi_numero)))
mi_numero_2=input("Ingrese su edad: ")
print("Su edad es: "+mi_numero_2)