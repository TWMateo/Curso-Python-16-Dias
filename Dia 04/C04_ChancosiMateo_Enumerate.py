#Como usar enumerate me sirve para acceder al valor y al indice de una lista, los objetos devueltos son tupples
mi_lista=[1,2,3,4,5,6]
print("Leyendo el objeto completo")
for nu in enumerate(mi_lista):
    print(nu)
print("Leyendo los valores del objeto por separado")
for ind,val in enumerate(mi_lista):
    print(ind,val)
