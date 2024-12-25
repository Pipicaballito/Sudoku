import timeit
from generatableros import mytablero
from generatableros import imprimir_tablero


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else '.' for num in fila))

def es_valido(tablero, fila, columna, num):
    for i in range(9):
        if tablero[fila][i] == num:
            return False
    for i in range(9):
        if tablero[i][columna] == num:
            return False
    sub_fila = fila // 3 * 3
    sub_columna = columna // 3 * 3
    for i in range(3):
        for j in range(3):
            if tablero[sub_fila + i][sub_columna + j] == num:
                return False
    return True

def encontrar_celda_vacia_mas_restrictiva(tablero):
    min_opciones = 10
    celda_mas_restrictiva = (-1, -1)
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                opciones = sum(1 for num in range(1, 10) if es_valido(tablero, fila, columna, num))
                if opciones < min_opciones:
                    min_opciones = opciones
                    celda_mas_restrictiva = (fila, columna)
    return celda_mas_restrictiva

def resolver_sudoku(tablero):
    fila, columna = encontrar_celda_vacia_mas_restrictiva(tablero)
    if fila == -1 and columna == -1:
        return True
    for num in range(1, 10):
        if es_valido(tablero, fila, columna, num):
            tablero[fila][columna] = num
            if resolver_sudoku(tablero):
                return True
            tablero[fila][columna] = 0
    return False

def resolver_y_medir_tiempo(tablero):
    tiempo_inicio = timeit.default_timer()
    resuelto = resolver_sudoku(tablero)
    tiempo_total = timeit.default_timer() - tiempo_inicio

    # Mostrar el tiempo de ejecución y el tablero resuelto
    if resuelto:
        print("\nTablero de Sudoku resuelto:")
        imprimir_tablero(tablero)
    else:
        print("No se encontró una solución válida.")
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} segundos")

tablero = mytablero

resolver_y_medir_tiempo(tablero)
