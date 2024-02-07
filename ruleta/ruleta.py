import random
import time

def inicializar_juego():
    return {
        'nombre': input("Digita tu nombre: "),
        'vidas_jugador': 3,
        'vidas_pc': 3,
        'nivel': 1
    }

def disparo(bala):
    if bala == 's':
        return True
    else:
        return False


def generar_comodines(max_comodines):
    comodines = ['corazon', 'navaja', 'lupa']
    
    max_comodines_por_tipo = 2

    # Generar comodines
    comodines_elegidos = []
    for _ in range(max_comodines):
        comodin = random.choice(comodines)
        if comodines_elegidos.count(comodin) < max_comodines_por_tipo:
            comodines_elegidos.append(comodin)

    return comodines_elegidos


def generar_balas(nivel):
    return ['s', 's', 'd', 'd'] + ['s', 'd'] * (nivel - 1)

def jugar_nivel(juego):
    print(f"\n¡¡BIENVENIDO A LA RULETA DEL DESTINO!! - Nivel {juego['nivel']}.\n")
    balas = generar_balas(juego['nivel'])
    # Generar comodines al inicio del nivel
    if juego['nivel'] > 1:
        max_comodines = 2 + (juego['nivel'] - 1)
    else:
        max_comodines = 3
    comodines_generados_jugador = generar_comodines(max_comodines)
    comodines_generados_pc = generar_comodines(max_comodines)

    
    while juego['vidas_jugador'] > 0 and juego['vidas_pc'] > 0:
        
        if len(balas) == 0:
            print("Recargando")
            for _ in range(5): 
                time.sleep(0.7)
                print(".", end="", flush=True)
            print("Recargado")
            balas = generar_balas(juego['nivel'])
        
        random.shuffle(balas)  # Mezcla las balas de manera aleatoria
        
        bala_seleccionada = balas[0]  # Toma la primera bala después de mezclar
        
        daño_bala = 1
        
        
        
        print(f"Estas son las vidas actuales:\n {juego['nombre']} = {juego['vidas_jugador']}.\n Enemigo = {juego['vidas_pc']}.\n")

        def accion():
            return disparo(bala_seleccionada)

        #agregar complementos en el nivel 2 en adelante
        nivel = juego['nivel']
        if nivel > 1:
           
            

            print(f"Hagamos las cosas más interesantes. Tienes los siguientes comodines:\n"
            f"Corazon: {comodines_generados_jugador.count('corazon')} te dan una nueva vida\n"
            f"Navaja: {comodines_generados_jugador.count('navaja')} causa el doble de daño\n"
            f"Lupa: {comodines_generados_jugador.count('lupa')} miras cual sera la siguiente bala")
            
            comodin_usado = input("Ahora seleciona si quieres usar un comodin Corazon con(c), Navaja con (n)y Lupa con (l)").lower()
            
            if comodin_usado == 'c':
                juego['vidas_jugador'] += 1
                time.sleep(0.5)
                print("Usaste el comodin del corazon vida +1")
                time.sleep(0.5)
                comodines_generados_jugador.remove('corazon')
            elif comodin_usado == 'n':
                daño_bala += 1
                time.sleep(0.5)
                print("Usaste el comodin de la navaja daño +1")
                time.sleep(0.5)
                comodines_generados_jugador.remove('navaja') 
            elif comodin_usado == 'l':
                time.sleep(0.5)
                
                print("Usaste el comodin de la Lupa el siguiente disparo sera")
                if bala_seleccionada == 's': 
                    print('Segura')
                else: 
                    print('Peligrosa')
                time.sleep(0.5)
                comodines_generados_jugador.remove('lupa')
            else:
                print("No se uso un comodin")             

        balas = balas[1:]  # Elimina la primera bala de la lista

        # Turno del jugador
        seleccion = input("Es hora de confiar en tu suerte. ¿A quién decides disparar? (Selecciona 1 para ti, 2 para el enemigo):\n ")
        
        print("Tu suerte dice", end="")
        for _ in range(4):  # 4 iteraciones para un total de 2 segundos (0.5s por iteración)
            time.sleep(0.5)
            print(".", end="", flush=True)
        
        if seleccion == '1':
            if accion():
                juego['vidas_pc'] -= daño_bala
                print("¡Salvado!")
            else:
                juego['vidas_jugador'] -= daño_bala
                print("¡Muerto!")
        elif seleccion == '2':
            if accion():
               juego['vidas_jugador'] -= daño_bala 
               print("¡Enemigo salvado!")
            else:
               juego['vidas_pc'] -= daño_bala
               print("¡Enemigo muerto!")
        
        
        if juego['vidas_jugador'] == 0:
            break
       
        
        # Turno de la PC
        random.shuffle(balas)  # Mezcla las balas de manera aleatoria
        bala_seleccionada_pc = balas[0]  # Toma la primera bala después de mezclar
        seleccion_pc = random.choice(['1', '2'])
        print("\nTurno de la PC:")
        
        
        if nivel > 1:
           
            
            print(f"El enemigo tiene los siguientes comodines:\n"
            f"Corazon: {comodines_generados_pc.count('corazon')} te dan una nueva vida\n"
            f"Navaja: {comodines_generados_pc.count('navaja')} causa el doble de daño\n"
            f"Lupa: {comodines_generados_pc.count('lupa')} miras cual sera la siguiente bala")
            

          
            
            comodin_usado =  random.choice(['c', 'n','l','']).lower()
            
            if comodin_usado == 'c':
                juego['vidas_pc'] += 1
                time.sleep(0.5)
                print("El enemigo uso el comodin del corazon vida +1")
                time.sleep(0.5)
                comodines_generados_pc.remove('corazon')
            elif comodin_usado == 'n':
                daño_bala += 1
                time.sleep(0.5)
                print("El enemigo uso el comodin de la navaja daño +1")
                time.sleep(0.5)
                comodines_generados_pc.remove('navaja') 
            elif comodin_usado == 'l':
                time.sleep(0.5)
                
                print("El enemigo uso el comodin de la Lupa el siguiente disparo sera")
                if bala_seleccionada_pc == 's': 
                    print('Segura')
                else: 
                    print('Peligrosa')
                time.sleep(0.5)
                comodines_generados_pc.remove('lupa')  
            else:
                print("El enemigo no uso un comodin")     
        
        
        
        balas = balas[1:]  # Elimina la primera bala de la lista
        
        
        print("La suerte del enemigo dice", end="")
        for _ in range(4):  # 4 iteraciones para un total de 2 segundos (0.5s por iteración)
            time.sleep(0.5)
            print(".", end="", flush=True)
        
        if seleccion_pc == '1':
            if accion():
                juego['vidas_jugador'] -= daño_bala
                print("¡Enemigo Salvado!")
            else:
                juego['vidas_pc'] -= daño_bala
                print("¡Enemigo Muerto!")
        elif seleccion_pc == '2':
            if accion():
               juego['vidas_pc'] -= daño_bala 
               print("¡Estas Salvado!")
            else:
               juego['vidas_jugador'] -= daño_bala
               print("¡Estas Muerto!")
        
    if juego['vidas_jugador'] <= 0:
        print("¡Has perdido todas tus vidas! ¡Juego terminado!")
        
        
    elif juego['vidas_pc'] <= 0:
        juego['nivel'] += 1
        juego['vidas_jugador'] = 3 + 1
        juego['vidas_pc'] = 3 + 1
        print("¡Enemigo derrotado! ¡Pasas al siguiente nivel!\n")
        print(f"\n¡Nivel {juego['nivel']} completado!\n")
        
    
    return juego


   

def main():
    juego = inicializar_juego()
    while juego['nivel'] <= 3 :  
        juego = jugar_nivel(juego)

    print("¡Juego terminado!")

if __name__ == "__main__":
    main()
