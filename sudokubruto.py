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
    sub_fila = (fila // 3) * 3
    sub_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[sub_fila + i][sub_columna + j] == num:
                return False
    return True

def resolver_sudoku_fuerza_bruta(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0: 
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if resolver_sudoku_fuerza_bruta(tablero):
                            return True
                        tablero[fila][columna] = 0  
                return False 
    return True  
def resolver_y_medir_tiempo(tablero):
    tiempo_inicio = timeit.default_timer()
    resuelto = resolver_sudoku_fuerza_bruta(tablero)
    tiempo_total = timeit.default_timer() - tiempo_inicio

    if resuelto:
        print("\nTablero de Sudoku resuelto:")
        imprimir_tablero(tablero)
    else:
        print("No se encontró una solución válida.")
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} segundos")

tablero = mytablero

resolver_y_medir_tiempo(tablero)
