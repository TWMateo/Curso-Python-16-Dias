#Al comprender las listas podemos trabajar con ellas para agregar elementos a ellas sin el uso de un for

palabra='Python'
print("Lista recorriendo una palabra")
mi_lista_uno=[letra for letra in palabra]
print(mi_lista_uno)

print("\nLista recorriendo valores y manipulandolos antes de añadirlos")
pies=[10,20,30,40,50]
lista_metros=[me*3.281 for me in pies]
print(lista_metros)

print("\nLista recorriendo valores y tomando en cuenta un if y else, si se quiere usar solo if entonces el if osea"
      " la condicion ira despues del for")

lista_en_rango=[num if num*2 > 10 else 'no' for num in range(0,21,2)]
print(lista_en_rango)