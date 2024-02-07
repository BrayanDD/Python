import random


def adivina_el_numero_computadora(x):
    
    print("Bienvenido")
    print(f"Seleciona un numero entre 1 y {x} para que la computadora intente adivinar")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    
    while respuesta != "c":
        #Generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else: 
            prediccion = limite_inferior #tambien podria ser el limite superior
        
        #obtenr derpuesta del usuario
        
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy baja ingresa la letra 'A' si es muy alta ingresa 'B' y si es correcta ingresa 'C': ").lower()
        
        if respuesta == "a":
            limite_superior = prediccion +1
            
        elif respuesta == "b":
            limite_superior = prediccion -1
    
    print(f"GENIAL!! la computadora adivino tu numero correctamente: {prediccion}")
    
adivina_el_numero_computadora(10)