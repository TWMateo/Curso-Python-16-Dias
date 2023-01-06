from random import *

numero_aleatorio= randint(1,100)
print(numero_aleatorio)
numero_ingresado=0
intentos=0
nombre_usuario=input("Cual es tu nombre:")
print(f"Bueno {nombre_usuario}, he pensado en un numero entre 1 y 100, tienes 8 intentos para adivinar cual es")

while(intentos<8):
    numero_ingresado=int(input("Ingresa tu numero escogido:"))
    if(numero_ingresado<1 or numero_ingresado>100):
        print("El numero que ingresaste no esta permitido")
    elif(numero_ingresado<numero_aleatorio):
        print("El numero ingresado es menor al numero secreto")
    elif(numero_ingresado>numero_aleatorio):
        print("El numero ingresado es mayor al numero secreto")
    elif(numero_ingresado==numero_aleatorio):
        print(f"Acertaste, el numero es el correcto y te tomo {intentos+1} intentos")
        break
    intentos+=1