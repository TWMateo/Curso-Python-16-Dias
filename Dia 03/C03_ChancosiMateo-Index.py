mi_texto="Texto de prueba"
resultado=mi_texto[0]
print("El caracter es: "+resultado)
buscado="prueba"
print("Posicion del caracter "+buscado+" es: {}".format(mi_texto.index(buscado)))
#Buscando u caracter en una posicion determinada
#Indicar el rango donde buscar la letra y devuelve la posicion donde se encuentra en caso de no encontrarse
#se retorna un error
print("Posicion del caracter entre el rango 5 a 12 es: {} ".format(mi_texto.index("o",4,11)))