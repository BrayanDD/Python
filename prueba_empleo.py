
entrada_usuario = input("Ingrese una serie de números separados por espacio: ")



# Convertir cada string a un número entero y almacenarlo en una lista
lista = [int(numero) for numero in entrada_usuario.split()]


def revert(lista):
    inicio = 0
    fin= len(lista) -1
    while inicio < fin:
        lista[inicio],lista[fin] = lista[fin],lista[inicio]
        inicio += 1
        fin -= 1
    return lista
     
print(revert(lista))