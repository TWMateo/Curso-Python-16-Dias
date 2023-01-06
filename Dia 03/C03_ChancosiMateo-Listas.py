#Probando el funcionamiento de las listas
mi_lista=['a','b',1,'d']
mi_lista2=['e','f','g','h']
#Tipo del elemento
print(type(mi_lista))
#Tamaño de la lista
print(len(mi_lista))
#Sacar un elemento a traves del indice
print("Elemento sacado a partir del indice: {}".format(mi_lista[1:4]))
#Concatenar listas
resultado=mi_lista2[::-1]
mi_lista3=mi_lista+mi_lista2
print(mi_lista3)
mi_lista3.append("g")
print(mi_lista3)
#Eliminar el ultimo de la lista con pop - El valor dentro de pop puede cambiar por el valor del indice del
#elemento que deseamos borrar
print(mi_lista3.pop())
print(mi_lista3)
#Ordenar la lista con el metodo sort
mi_lista4=['z','m','n','a','b']
print(mi_lista4)
mi_lista4.sort()
print(mi_lista4)
#Se puede ordenar al reves a lista con el metodo reverse
mi_lista4.reverse()
print(mi_lista4)