nombre_obrero=input("Ingrese su nombre: ")
valor_vendido=float(input("Ingrese el monto vendido: "))
print("Ok {}.Este mes ganaste: ${}".format(nombre_obrero,round((valor_vendido*13)/100,2)))