#El metodo min y el metodo max retornan el valor minimo y el valor maximo respectivamente
#estos valores pueden ser obtenidos de una lista de numeros o letra y de diccionarios en los cuales se
#evaluara el campo de termino para saber cual es mayor de entre los elementos del diccionario.

menor=min(12,14,1,5,30)
mayor=max('Mateo','Zoe','Fernanda')

print(f"El menor valor de la lista de numeros es {menor}")
print(f"El nombre maximo de la lista de nombres es {mayor}")

#Usando diccionarios se usara el campo de termino para evaluar cual termino es maypr y el campo
#de valor se lo usara para la evaluacion cuando se acceda a el a traves del atributo .values().

diccionario={'Uno':1,'Dos':2,'Tres':3}
menor_dicc=min(diccionario.values())
mayor_dicc=max(diccionario.values())
print(f"El mayor valor del diccionario es {mayor_dicc} el menor valor es {menor_dicc}")