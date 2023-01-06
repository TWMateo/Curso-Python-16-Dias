#upper() - Tranforma a mayusculas
#lower() - Transforma a minusculas
#split() - Separa la palabra en partes (lista)
#join() - Une listas usando un separador
#find() - Encuentra un substring
#replace() - Remplazar un substring
texto="Este es el metodo de Mateo"
resultado=texto

print(resultado)
#Conversion a mayusculas
print(resultado.upper())
print(resultado[1].upper())
#Conversion a minusculas
print(resultado.lower())
#Subdivide el String en un arreglo de strings
print(resultado.split())
#Se subdividio el String hasta la t siendo esta letra la bandera de separacion del string
print("Split con bandera : {}".format(resultado.split("t")))

#USO DEL JOIN
a="Aprender"
b="Python"
c="es"
d="lo"
e="mejor"
f="-".join([a,b,c,d,e])
print(f)
#Uso de FIND
print(resultado.find("de"))
#Uso de REPLACE
print(resultado.replace("Mateo","Franco"))