#Es la union entre listas - El tamaño del zip es igual al tamaño de la lista mas corta
lista_uno=['Ana','Hugo','Valeria']
lista_dos=[65,29,42]
lista_ciudades=['Otavalo','Madrid','Lima']
combinados=zip(lista_uno,lista_dos,lista_ciudades)
combi_lista=list(combinados)
print(list(combinados))

for nombre,edad,ciudad in combi_lista:
    print(f"{nombre} {edad} {ciudad}")


lista_uno=['uno','um','one']
lista_dos=['dos','dois','two']
lista_tres=['tres','três','three']
lista_cuatro=['cuatro','quatro','four']
lista_cinco=['cinco','cinco','five']

numeros=list(zip(lista_uno,lista_dos,lista_tres,lista_cuatro,lista_cinco))
print(numeros)