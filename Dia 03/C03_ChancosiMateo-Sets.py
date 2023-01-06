#Los set son inmutables (no podemos buscar a los elementos por su posicion) es decir que no permiten dentro de ellos
#ni listas ni diccionarios y tampoco pueden existir valores repetidos dentro de
#los mismos
set_1=set((1,2,3))
print(type(set_1))
set_2={1,2,3,('a','b')}
print(type(set_2))
print(set_2)
#Consultas en los sets
print(2 in set_1)
#Unir sets - Si es que hay algun elemento repetido al unir se lo elimina
set_3={3,4,5}
set_4=set_1.union(set_3)
print(set_4)
#Agregar nuevos elementos a los sets

set_4.add(5)
set_4.add(6)
print(set_4)

#Elimiar elementos con remove - Causa error si el elemento que se quiere eliminar no existe en la lista
#Descartar elementos con discard - NO causa error si el elemento que se quiere elminar no existe en el set
#set_4.remove(6)
set_4.discard(6)
print(set_4)

#Se puede eliminar el elemento que este en primer lugar del set con el metodo pop
set_4.pop()
print(set_4)

#Con el metodo clear se limpiar el set o se elimina los elementos de dentro
set_4.clear()
print(set_4)


