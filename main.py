
from lista import habilitadas  # lista grande
import time

# Lista pequeña para el ejemplo con Burbuja
lista_pequena = [50, 5231, 66, 23, 2387, 195, 2]

def burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = []
        mayores = []
        for elemento in lista[1:]:
            if elemento <= pivote:
                menores.append(elemento)
            else:
                mayores.append(elemento)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

def busqueda_lineal(lista, busqueda):
    for a in range(len(lista)):
        if lista[a] == busqueda:
            return a
    return -1

def busqueda_binaria(lista, busqueda):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == busqueda:
            return medio
        elif lista[medio] < busqueda:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def menu_ordenar():
    print("\nElija método de ordenamiento:")
    print("1. Burbuja (solo lista pequeña, ejemplo didáctico)")
    print("2. Quick Sort (lista grande, recomendado)")
    opcion = input("Ingrese opción (1/2): ")
    return opcion

def menu_busqueda():
    print("\nElija método de búsqueda:")
    print("1. Lineal")
    print("2. Binaria (solo en listas ordenadas)")
    opcion = input("Ingrese opción (1/2): ")
    return opcion

while True:
        print("\nMenú principal")
        print("1. Ordenar y buscar en lista pequeña (Burbuja)")
        print("2. Ordenar y buscar en lista grande (Quick Sort)")
        print("3. Salir")
        eleccion = input("Ingrese su opción: ")

        if eleccion == "1":
            print(f"\nLista pequeña original:\n{lista_pequena}")
            op_ord = menu_ordenar()
            if op_ord == "1":
                t1 = time.time()
                lista_ordenada = burbuja(lista_pequena)
                t2 = time.time()
                print(f"Lista ordenada (Burbuja): {lista_ordenada}")
                print(f"Tiempo de ordenamiento: {t2 - t1:.6f} segundos")
            else:
                print("Quick Sort no es necesario en lista pequeña para el ejemplo.")
                continue

            buscar = int(input("Ingrese número a buscar: "))
            op_busq = menu_busqueda()
            if op_busq == "1":
                t1 = time.time()
                pos = busqueda_lineal(lista_pequena, buscar)
                t2 = time.time()
                metodo = "Lineal"
                lista_mostrar = lista_pequena
            else:
                t1 = time.time()
                pos = busqueda_binaria(lista_ordenada, buscar)
                t2 = time.time()
                metodo = "Binaria"
                lista_mostrar = lista_ordenada

            if pos != -1:
                print(f"Encontrado en posición {pos} ({metodo}, lista {lista_mostrar})")
            else:
                print("NO encontrado")
            print(f"Tiempo de búsqueda: {t2 - t1:.6f} segundos")

        elif eleccion == "2":
            print(f"\nLista grande de {len(habilitadas)} registros.")
            t1 = time.time()
            lista_ordenada = quick_sort(habilitadas)
            t2 = time.time()
            print(f"Lista ordenada con Quick Sort (solo muestra los primeros 10): {lista_ordenada[:10]} ...")
            print(f"Tiempo de ordenamiento: {t2 - t1:.3f} segundos")

            buscar = int(input("Ingrese número a buscar: "))
            op_busq = menu_busqueda()
            if op_busq == "1":
                t1 = time.time()
                pos = busqueda_lineal(habilitadas, buscar)
                t2 = time.time()
                metodo = "Lineal"
                lista_mostrar = habilitadas
            else:
                t1 = time.time()
                pos = busqueda_binaria(lista_ordenada, buscar)
                t2 = time.time()
                metodo = "Binaria"
                lista_mostrar = lista_ordenada

            if pos != -1:
                print(f"Encontrado en posición {pos} ({metodo})")
            else:
                print("NO encontrado")
            print(f"Tiempo de búsqueda: {t2 - t1:.6f} segundos")

        elif eleccion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")
