# Sudoku Solver con Backtracking y Forward Checking

## Descripción
Este proyecto implementa un solucionador de Sudoku utilizando tres enfoques diferentes:
1. **Fuerza Bruta (FB)**: Prueba todas las combinaciones posibles hasta encontrar una solución.
2. **Backtracking (BT)**: Optimiza la búsqueda utilizando un método de retroceso inteligente.
3. **Backtracking con Forward Checking (BT-FC)**: Mejora la eficiencia reduciendo el espacio de búsqueda mediante la eliminación de valores no válidos antes de hacer elecciones.

## Estructura del Código
- `solucion1_FB(tablero)`: Resuelve el Sudoku con un enfoque de fuerza bruta.
- `solucion2_BT(tablero)`: Implementa backtracking seleccionando la mejor celda con menor cantidad de opciones disponibles.
- `solucion3_BT_FC(tablero)`: Utiliza backtracking con comprobación hacia adelante, eliminando valores imposibles antes de cada decisión.
- `probar_algoritmo(funcion, tablero)`: Evalúa el desempeño de cada algoritmo en términos de intentos y tiempo de ejecución.

## Uso
Para ejecutar el programa, simplemente ejecuta el script en Python:
```bash
python sudoku_solver.py
```
El script probará automáticamente los tres algoritmos sobre un tablero de Sudoku predefinido.

## Ejemplo de Tablero de Entrada
```python
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
```

## Resultados
El programa mostrará el tiempo de ejecución y la cantidad de intentos realizados por cada algoritmo.

## Requisitos
- Python 3.x

## Autor
Desarrollado por un estudiante de Ingeniería de Sistemas apasionado por la inteligencia artificial y la optimización de algoritmos. 🚀