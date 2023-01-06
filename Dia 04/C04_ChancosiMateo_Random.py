#Para usar el metodo randint lo que se debe hacer es importar la libreria random - en este caso se importo todos
#los metodos de la libreria random en lugar de uno a uno.
from random import *
#Devuleve un valor aleatorio entero
aleatorio=randint(1,20)
#Devuelve un valor aleatorio decimal
aleatorio_decimal=round(uniform(1,5),1)
#El metodo random da un numero aleatorio decimal entre 0 y uno
aleatorio_randomico=random()

print(f"Numero aleatorio randomico {aleatorio_randomico}")
print(f"Numero aleatroio entero {aleatorio}")
print(f"Numero aleatorio decimal {aleatorio_decimal}")

#Escoger un elemento aleatorio de una lista u otro coleccionable
lista=['azul','rojo','rosado']
aleatorio_color=choice(lista)
print(f"Color aleatorio {aleatorio_color}")

#Metodo shuffle ordena de manera aleatoria una lista
lista_numeros=[1,2,3,4,5,6,7,8,9]
shuffle(lista_numeros)
print(f"Impresion de una lista de numeros: {lista_numeros}")
