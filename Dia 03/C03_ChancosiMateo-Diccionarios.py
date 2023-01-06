diccionario={'c1':1,'c2':'valor 1'}
print(diccionario)
#Imprimiendo el contenido de la definicion c2
print(diccionario['c2'])
print(diccionario['c1'])
#Diccionario dentro de un diccionario o una lista
dicDic={'c1':'55','c2':[22,44,66],'c3':{'a1':11,'a2':'Mateo'}}
#Si quiero un elemento interno de la lista o
#diccionario dentro de este diccionario se
#adjuntara un par de corchetes mas y la posicion
#o clave del elemento a consultar
print(dicDic['c3']['a1'])
#EJERCICIO: En una linea de codigo imprimir la letra e
#del siguiente diccionario
dic={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())
#EJEMPLO - Ingresando un nuevo valor
dic2={1:'a',2:'b'}
print(dic2)
dic2['definicion3']='c'
print(dic2)
#Sobreescribir valores en el diccionario
dic2[1]='Sobreescrito'
print(dic2)
#Obtener todas las claves del diccionario
print(dic2.keys())
#Obtener todos los elementod del diccionario
print(dic2.items())