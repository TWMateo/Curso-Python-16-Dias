#Un string puede ser multiplicable
nombre="Be"
print(nombre*10)
#Un string puede contener saltos de linea sin \n
poema="Hola \n mundo"
poema2="""Hola 
mundo
probando 
las
propiedades"""
print(poema)
print("Poema usando las triples comillas "+poema2)
#Compruebo si existe una palabra en el string
print("probando" in poema2)
#Comprueba si no existe una palabra dentro del string
print("Mateo" not in poema2)
#Devuelve el tamaño del string
print(len(poema))