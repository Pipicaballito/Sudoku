import random

def generar_tablero_sudoku(dificultad="medio"):
    # Crear un tablero vacío
    mytablero = [[0 for _ in range(9)] for _ in range(9)]
    
    # Generar un mytablero completo utilizando backtracking
    if not llenar_tablero(mytablero):
        return None
    
    # Eliminar celdas según la dificultad
    quitar_celdas(mytablero, dificultad)
    
    return mytablero

def llenar_tablero(mytablero):
    # Función recursiva para llenar el mytablero usando backtracking
    for fila in range(9):
        for columna in range(9):
            if mytablero[fila][columna] == 0:
                numeros_posibles = list(range(1, 10))
                random.shuffle(numeros_posibles)
                for num in numeros_posibles:
                    if es_valido(mytablero, fila, columna, num):
                        mytablero[fila][columna] = num
                        if llenar_tablero(mytablero):
                            return True
                        mytablero[fila][columna] = 0
                return False
    return True

def es_valido(mytablero, fila, columna, num):
    # Comprobar si el número es válido en la posición dada
    # Comprobar fila
    if num in mytablero[fila]:
        return False
    
    # Comprobar columna
    for i in range(9):
        if mytablero[i][columna] == num:
            return False
    
    # Comprobar subcuadro 3x3
    fila_inicio = (fila // 3) * 3
    columna_inicio = (columna // 3) * 3
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if mytablero[i][j] == num:
                return False
    
    return True

def quitar_celdas(mytablero, dificultad):
    # Establecer el número de celdas a quitar según la dificultad
    if dificultad == "fácil":
        celdas_a_quitar = 30
    elif dificultad == "medio":
        celdas_a_quitar = 45
    elif dificultad == "difícil":
        celdas_a_quitar = 60
    
    while celdas_a_quitar > 0:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if mytablero[fila][columna] != 0:
            mytablero[fila][columna] = 0
            celdas_a_quitar -= 1

def imprimir_tablero(mytablero):
    # Imprimir el mytablero de forma más legible
    for i, fila in enumerate(mytablero):
        for j, num in enumerate(fila):
            if num == 0:
                print('.', end=" ")  # Mostrar '.' para las celdas vacías
            else:
                print(num, end=" ")
            # Para separar los subcuadros de 3x3 con espacios
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()  # Nueva línea después de cada fila
        
        # Separación de los bloques 3x3 con una línea horizontal
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

# Generar un mytablero de Sudoku con dificultad "medio"
mytablero = generar_tablero_sudoku("medio")
print("Tablero de Sudoku:")
imprimir_tablero(mytablero)
