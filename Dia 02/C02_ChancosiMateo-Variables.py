from builtins import input
#1. El nombre de las variables debe ser legible
#2. El nombre de la variable debe ser compuesta por solo una unidad de texto
#En python se acotumbra a hacer esto: nombre_de_estudiante
#Se usa solo minusculas y los guiones bajos
#3. No usar tildes ni ñ
#4. Solo se pueden usar numeros al final del nombre de la variable
#5. No se pueden usar palabras reservadas
#6. Los nombres de variables no pueden contener simbolos
nombre="Juan"
print(nombre)
numero=30
numero2=50
suma=numero+numero2
sumaString="{}+{}=".format(numero,numero2)
nombreMascota=input("Ingrese el nombre de su mascota: ")
print("Imprimiendo numeros: {} {} {}".format(numero,numero2,nombreMascota))
print("Sumatoria de "+sumaString+" {}".format(suma))

