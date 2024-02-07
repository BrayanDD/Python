import random
import string

from ahorcado_diagrama import vidas_diccionario_visual
from palabras import palabras


def obetener_palabra_valida(palabras):
    #Seleccionar palabras al azar de palabras validas
    palabra = random.choice(palabras)

    while '-' in palabra  or '' in palabra :
        palabra = random.choice(palabras)
        
    return palabra.upper()



def ahorcado():

    print("! Bienvenido ¡")

    palabra = obetener_palabra_valida(palabras)
    
   
        
    letras_por_adivinar = set(palabra) 
    abedecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    
    vidas = 7
    
    while len(letras_por_adivinar)>0 and vidas >  0:
        print(f"Te quedan {vidas} vidas y has usado estasa letras: {''.join(letras_adivinadas)}")
        
        #Mostrar estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]    
        #Estado ahorcado
        print(vidas_diccionario_visual[vidas])
        
        #estado palabras
        print(f"Palabra {' '.join(palabra_lista)}")
        
        letra_usuario= input("Escoge una letra : ".upper())
        
        #verificar letra escogida 
        if letra_usuario in abedecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #si la letra está en l a palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vidas -= 1
                print(f"Tú letra, {letra_usuario} no está en la palabra")
        
        elif  letra_usuario in letras_adivinadas:
            print(f"\nYa escogiste esta letra ")
        else: 
            print("\nEsta letra no es valida")
    
    #resultados
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado!! Perdiste. La palabra era: {palabra}")
    else:
        print(f"Excelente!! adivinaste la palabra {palabra}")    

ahorcado()