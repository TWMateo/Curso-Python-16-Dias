#Uso del FOR

lista_uno=['a','b','c','d']
for letra in lista_uno:
    print("Impresion del indice de la letra: {}".format(lista_uno.index(letra)+1))
    print("Letra "+letra)

#Crear un for con una condicion

nombres=['Juan','Pedro','Lucas','Lucia']
letra="L"
print(f"Impresion de los nombres que empiezen con {letra}")
for nom in nombres:
    print(type(nom))
    if nom.startswith(letra):
        print(f"El nombre es: {nom}")

#Crear un for que recorra una lista de numeros y los recorra

lista_numeros=[1,2,3,4,5]
sumatoria=0
for num in lista_numeros:
    sumatoria+=num
    print(f"Total sumatoria: {sumatoria}")

#Crear un for que deletree una palabra
print("Deletreo de nombres: ")
for letr in "Mateo y Mafer":
    print(letr)

#Leer listas dentro de otras listas se crean tantas variables como datos a leer o sino se puede leer el
#objeto completo
print("Impresion de listas compuestas:")
lista_compuesta=[[1,2],[3,4],[5,6]]
for a,b in lista_compuesta:
    print(a)
    print(b)

#Recorrido de diccionario para esto se necesita dos items uno que lea el terminoo y el otro el signficado
print("Impresion de un diccionario")
diccionario_uno={"Valor1":1,"Valor2":"5",'Valor3':6}

for a,b in diccionario_uno.items():
    print(a)
    print(b)