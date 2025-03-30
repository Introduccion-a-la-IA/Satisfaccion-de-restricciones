import time

contador_intentos = 0  # Contador de intentos realizados

def encontrar_espacio_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return None, None


def movimiento_valido(tablero, fila, col, num):
    # Verificar fila
    for x in range(9):
        if tablero[fila][x] == num:
            return False
    
    # Verificar columna
    for x in range(9):
        if tablero[x][col] == num:
            return False
    
    # Verificar subgrilla 3x3
    fila_inicial, col_inicial = 3 * (fila // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if tablero[i + fila_inicial][j + col_inicial] == num:
                return False
    return True


def impresion(tablero):    
    for fila in tablero:
        print(fila)
        
        
        
def solucion1_FB(tablero):
    global contador_intentos
    fila, col = encontrar_espacio_vacio(tablero)
    
    if fila is None:  # Si no hay espacios vacíos, el tablero está completo
        return tablero
    
    for num in range(1, 10):  # Prueba del 1 al 9
        if movimiento_valido(tablero, fila, col, num):
            tablero[fila][col] = num  # Intentamos colocar el número
            contador_intentos += 1  # Contar intento
            
            resultado = solucion1_FB(tablero)  # Llamada recursiva
            if resultado:
                return resultado  # Si encuentra solución, la retorna
            
            tablero[fila][col] = 0  # Retrocede si no funciona
    
    return False  # No hay solución



def solucion2_BT(tablero):
    global contador_intentos  

    def obtener_posibilidades(fila, col):
        posibilidades = set(range(1, 10))
        for x in range(9):
            posibilidades.discard(tablero[fila][x])  
            posibilidades.discard(tablero[x][col])  
        
        fila_inicial, col_inicial = 3 * (fila // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                posibilidades.discard(tablero[fila_inicial + i][col_inicial + j])
        
        return list(posibilidades)

    def obtener_mejor_celda():
        mejor_fila, mejor_col = None, None
        mejor_opciones = 10  
        for i in range(9):
            for j in range(9):
                if tablero[i][j] == 0:
                    opciones = obtener_posibilidades(i, j)
                    if len(opciones) < mejor_opciones:
                        mejor_opciones = len(opciones)
                        mejor_fila, mejor_col = i, j
        return mejor_fila, mejor_col

    def backtrack():
        global contador_intentos
        fila, col = obtener_mejor_celda()  
        if fila is None:
            return True  

        for num in obtener_posibilidades(fila, col):  
            contador_intentos += 1  
            tablero[fila][col] = num  
            if backtrack():
                return True
            tablero[fila][col] = 0  

        return False

    resultado = backtrack()
    return tablero if resultado else False


#def solucion3_BT_FC(tablero):
    
    #return True or False 

import time

def probar_algoritmo(funcion, tablero):
    global contador_intentos
    contador_intentos = 0  # Resetear intentos antes de cada prueba
    
    # Copia del tablero para no modificar el original
    tablero_copia = [fila[:] for fila in tablero]
    
    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    resultado = funcion(tablero_copia)
    fin = time.perf_counter()

    # Imprimir resultados
    print(f"\n🔹 {funcion.__name__}:")
    print(f"   ⏳ Tiempo de ejecución: {fin - inicio:.10f} segundos.")
    print(f"   🎯 Intentos realizados: {contador_intentos}")
    if resultado:
        print("   ✅ Sudoku resuelto correctamente.")
    else:
        print("   ❌ No se encontró solución.")

if __name__ == "__main__":
    tablero = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]


    probar_algoritmo(solucion1_FB, tablero)
    probar_algoritmo(solucion2_BT, tablero)
    #probar_algoritmo(solucion3_BT_FC, tablero)
    
    
    print("\nSolución:")
    resultado = solucion2_BT(tablero)
    if isinstance(resultado, str):
        print(resultado)
    else:
        for fila in resultado:
            print(fila)
