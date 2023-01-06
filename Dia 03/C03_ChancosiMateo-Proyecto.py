texto=input("Ingrese un texto: ")
letras_ingresadas=[]
letras_ingresadas.append(input("Ingrese una letra: ").lower())
letras_ingresadas.append(input("Ingrese una letra: ").lower())
letras_ingresadas.append(input("Ingrese una letra: ").lower())
#Primer apartado
print("Lista de letras ingresadas:\n{}".format(letras_ingresadas))
print("La letra {} aparece {} veces".format(letras_ingresadas[0],texto.count(letras_ingresadas[0])+
                                            texto.count(letras_ingresadas[0].upper())))
print("La letra {} aparece {} veces".format(letras_ingresadas[1],texto.count(letras_ingresadas[1])+
                                            texto.count(letras_ingresadas[1].upper())))
print("La letra {} aparece {} veces".format(letras_ingresadas[2],texto.count(letras_ingresadas[2])+
                                            texto.count(letras_ingresadas[2].upper())))
#Segundo apartado
lista_palabras=texto.split()
print("Hay {} palabras en el texto".format(len(lista_palabras)))
#Tercer apartado
print("Primer letra del texto es: \"{}\"\nLa ultima letra del texto es: \"{}\"".format(texto[0],texto[-1]))
#Cuarto punto - Revertir el orden de las palabras
lista_palabras.reverse()
oracion_unida=" ".join(lista_palabras)
print("Texto al reves: {}".format(oracion_unida))
#Quinto punto - La palabra python se encuentra en el texto
if "python" in texto:
    print("La palabra python se encuentra en el texto")
else:
    print("No se encuentra la palabra python")