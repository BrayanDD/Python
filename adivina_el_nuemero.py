import random


def adivina_el_numero(x):
    print("Bienvenido a adivina el numero!!!")
    print("Tu objetivo es adivinar el número generado por la computadora.")
    numero_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y x.
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        #el usuario ingresa un numero
        prediccion = int(input(f"adivina el numero entre 1 y {x}: "))
        if prediccion < numero_aleatorio :
            print("intenta otra vez . el numero es mayor. ")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez . el numero es menor. ")
    print(f"Es correcto !! el numero {prediccion} es el correcto")


adivina_el_numero(10)