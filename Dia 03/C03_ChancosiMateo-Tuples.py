#Tuples son inmutables (por ende no e pueden incluir listas ni diccionarios dentro de estos)
#Son mejores a las listas debido a su eficiencia
#ya que ocupan menoos espacio de memoria y no permiten
#reasignar valores

mi_tuple=(1,2,(10,20),4,5)
mi_tuple2=(1,5.4,'ff')
print(type(mi_tuple))
print(mi_tuple[2][0])
#Se puede hacer casting a listas
mi_lista=list(mi_tuple)
print(type(mi_lista))
print(mi_lista)
#Se pueden desempacar los valores dentro del tuple
#dando la misma cantidad de variables que de
#valores los cuales se desempacaran
t=(1,2,3)
x,y,z=t
print(x,y,z)

