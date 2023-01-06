#Uso del loop while
numero=5
while numero>0:
    print(numero)
    numero-=1
else:
    print("No queda mas dinero")

#Detener while con un input
continuar='s'
while continuar=='s':
    continuar=input("Desea continuar? s/n")
else:
    print("Gracias")