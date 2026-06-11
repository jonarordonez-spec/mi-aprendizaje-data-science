"""
Script de apoyo - Clase 5: Algebra Lineal con NumPy
Autor: Jonathan Ruiz Ordoñez
Fecha: 29 de Octubre 2024
Descripción: Operaciones de álgebra lineal con NumPy - Vectores y Matrices
"""

import numpy as np

def demostrar_vectores():
    """Demuestra operaciones con vectores en NumPy"""
    print("=" * 50)
    print(" VECTORES EN NUMPY")
    print("=" * 50)
    
    # Creación de vectores
    vector_python = [1, 2, 3, 4, 5]
    vector_numpy = np.array([1, 2, 3, 4, 5])
    vector_unos = np.ones(5)
    vector_rango = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
    
    print("Lista Python:", vector_python)
    print("Vector NumPy:", vector_numpy)
    print("Vector de unos:", vector_unos)
    print("Vector con arange:", vector_rango)
    
    # Operaciones con vectores
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([4, 5, 6])
    
    print(f"\nVector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Suma: {vector_a + vector_b}")
    print(f"Resta: {vector_a - vector_b}")
    print(f"Multiplicación elemento-wise: {vector_a * vector_b}")
    
    # Producto punto y norma
    producto_punto = np.dot(vector_a, vector_b)
    norma_a = np.linalg.norm(vector_a)
    
    print(f"Producto punto AB: {producto_punto}")
    print(f"Norma del vector A: {norma_a:.2f}")
    
    return vector_a, vector_b

def demostrar_matrices():
    """Demuestra operaciones con matrices en NumPy"""
    print("\n" + "=" * 50)
    print(" MATRICES EN NUMPY")
    print("=" * 50)
    
    # Creación de matrices
    matriz_a = np.array([[1, 2], [3, 4]])
    matriz_b = np.array([[5, 6], [7, 8]])
    matriz_identidad = np.eye(2)  # Matriz identidad 2x2
    
    print("Matriz A:")
    print(matriz_a)
    print("\nMatriz B:")
    print(matriz_b)
    print("\nMatriz Identidad:")
    print(matriz_identidad)
    
    # Propiedades de matrices
    print(f"\nDimensiones de A: {matriz_a.shape}")
    print(f"Total elementos en A: {matriz_a.size}")
    
    # Operaciones con matrices
    print("\n--- Operaciones Matriciales ---")
    print("Suma A + B:")
    print(matriz_a + matriz_b)
    
    print("\nMultiplicación elemento-wise A * B:")
    print(matriz_a * matriz_b)
    
    print("\nMultiplicación de matrices A @ B:")
    print(matriz_a @ matriz_b)
    
    # Multiplicación por escalar
    print("\nMatriz A * 2:")
    print(matriz_a * 2)
    
    # Matriz transpuesta
    print("\nMatriz A transpuesta:")
    print(matriz_a.T)
    
    return matriz_a, matriz_b, matriz_identidad

def comparar_python_numpy():
    """Compara operaciones entre listas Python y arrays NumPy"""
    print("\n" + "=" * 50)
    print(" COMPARACION: LISTAS PYTHON vs ARRAYS NUMPY")
    print("=" * 50)
    
    # Listas Python
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    
    # Arrays NumPy
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])
    
    print("Listas Python:")
    print(f"  Lista A: {lista_a}")
    print(f"  Lista B: {lista_b}")
    print("  Suma manual: [a+b for a,b in zip(lista_a, lista_b)]")
    
    print("\nArrays NumPy:")
    print(f"  Array A: {array_a}")
    print(f"  Array B: {array_b}")
    print(f"  Suma directa: {array_a + array_b}")
    
    print("\n NumPy permite operaciones matemáticas directas")
    print(" Más eficiente para cálculos numéricos")
    print(" Optimizado para álgebra lineal")

def ejercicios_practicos():
    """Ejercicios prácticos de álgebra lineal"""
    print("\n" + "=" * 50)
    print(" EJERCICIOS PRACTICOS")
    print("=" * 50)
    
    # Ejercicio 1: Sistema de ecuaciones simple
    print("Ejercicio 1: Resolver sistema de ecuaciones")
    A = np.array([[2, 1], [1, 3]])
    b = np.array([5, 10])
    
    try:
        solucion = np.linalg.solve(A, b)
        print(f"Sistema: 2x + y = 5, x + 3y = 10")
        print(f"Solución: x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución única")
    
    # Ejercicio 2: Distancia entre puntos
    print("\nEjercicio 2: Distancia entre puntos en 3D")
    punto1 = np.array([1, 2, 3])
    punto2 = np.array([4, 6, 8])
    distancia = np.linalg.norm(punto1 - punto2)
    print(f"Punto 1: {punto1}")
    print(f"Punto 2: {punto2}")
    print(f"Distancia: {distancia:.2f}")

if __name__ == "__main__":
    print(" CLASE 5 - ALGEBRA LINEAL CON NUMPY")
    print("Jonathan Ruiz Ordoñez - 29 Oct 2024")
    print("=" * 60)
    
    vectores = demostrar_vectores()
    matrices = demostrar_matrices()
    comparar_python_numpy()
    ejercicios_practicos()
    
    print("\n" + "=" * 50)
    print(" CLASE 5 COMPLETADA - FUNDAMENTOS DE ALGEBRA LINEAL")
    print("=" * 50)
    print(" Conceptos dominados:")
    print("    Vectores y operaciones vectoriales")
    print("    Matrices y operaciones matriciales")
    print("    Producto punto y normas")
    print("    Matriz identidad y transpuesta")
    print("    Diferencias Python vs NumPy")
cat > helpers_clase5.py << 'EOF'
"""
Script de apoyo - Clase 5: Algebra Lineal con NumPy
Autor: Jonathan Ruiz Ordoñez
Fecha: 29 de Octubre 2024
Descripción: Operaciones de álgebra lineal con NumPy - Vectores y Matrices
"""

import numpy as np

def demostrar_vectores():
    """Demuestra operaciones con vectores en NumPy"""
    print("=" * 50)
    print(" VECTORES EN NUMPY")
    print("=" * 50)
    
    # Creación de vectores
    vector_python = [1, 2, 3, 4, 5]
    vector_numpy = np.array([1, 2, 3, 4, 5])
    vector_unos = np.ones(5)
    vector_rango = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
    
    print("Lista Python:", vector_python)
    print("Vector NumPy:", vector_numpy)
    print("Vector de unos:", vector_unos)
    print("Vector con arange:", vector_rango)
    
    # Operaciones con vectores
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([4, 5, 6])
    
    print(f"\nVector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Suma: {vector_a + vector_b}")
    print(f"Resta: {vector_a - vector_b}")
    print(f"Multiplicación elemento-wise: {vector_a * vector_b}")
    
    # Producto punto y norma
    producto_punto = np.dot(vector_a, vector_b)
    norma_a = np.linalg.norm(vector_a)
    
    print(f"Producto punto AB: {producto_punto}")
    print(f"Norma del vector A: {norma_a:.2f}")
    
    return vector_a, vector_b

def demostrar_matrices():
    """Demuestra operaciones con matrices en NumPy"""
    print("\n" + "=" * 50)
    print(" MATRICES EN NUMPY")
    print("=" * 50)
    
    # Creación de matrices
    matriz_a = np.array([[1, 2], [3, 4]])
    matriz_b = np.array([[5, 6], [7, 8]])
    matriz_identidad = np.eye(2)  # Matriz identidad 2x2
    
    print("Matriz A:")
    print(matriz_a)
    print("\nMatriz B:")
    print(matriz_b)
    print("\nMatriz Identidad:")
    print(matriz_identidad)
    
    # Propiedades de matrices
    print(f"\nDimensiones de A: {matriz_a.shape}")
    print(f"Total elementos en A: {matriz_a.size}")
    
    # Operaciones con matrices
    print("\n--- Operaciones Matriciales ---")
    print("Suma A + B:")
    print(matriz_a + matriz_b)
    
    print("\nMultiplicación elemento-wise A * B:")
    print(matriz_a * matriz_b)
    
    print("\nMultiplicación de matrices A @ B:")
    print(matriz_a @ matriz_b)
    
    # Multiplicación por escalar
    print("\nMatriz A * 2:")
    print(matriz_a * 2)
    
    # Matriz transpuesta
    print("\nMatriz A transpuesta:")
    print(matriz_a.T)
    
    return matriz_a, matriz_b, matriz_identidad

def comparar_python_numpy():
    """Compara operaciones entre listas Python y arrays NumPy"""
    print("\n" + "=" * 50)
    print(" COMPARACION: LISTAS PYTHON vs ARRAYS NUMPY")
    print("=" * 50)
    
    # Listas Python
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    
    # Arrays NumPy
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])
    
    print("Listas Python:")
    print(f"  Lista A: {lista_a}")
    print(f"  Lista B: {lista_b}")
    print("  Suma manual: [a+b for a,b in zip(lista_a, lista_b)]")
    
    print("\nArrays NumPy:")
    print(f"  Array A: {array_a}")
    print(f"  Array B: {array_b}")
    print(f"  Suma directa: {array_a + array_b}")
    
    print("\n NumPy permite operaciones matemáticas directas")
    print(" Más eficiente para cálculos numéricos")
    print(" Optimizado para álgebra lineal")

def ejercicios_practicos():
    """Ejercicios prácticos de álgebra lineal"""
    print("\n" + "=" * 50)
    print(" EJERCICIOS PRACTICOS")
    print("=" * 50)
    
    # Ejercicio 1: Sistema de ecuaciones simple
    print("Ejercicio 1: Resolver sistema de ecuaciones")
    A = np.array([[2, 1], [1, 3]])
    b = np.array([5, 10])
    
    try:
        solucion = np.linalg.solve(A, b)
        print(f"Sistema: 2x + y = 5, x + 3y = 10")
        print(f"Solución: x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución única")
    
    # Ejercicio 2: Distancia entre puntos
    print("\nEjercicio 2: Distancia entre puntos en 3D")
    punto1 = np.array([1, 2, 3])
    punto2 = np.array([4, 6, 8])
    distancia = np.linalg.norm(punto1 - punto2)
    print(f"Punto 1: {punto1}")
    print(f"Punto 2: {punto2}")
    print(f"Distancia: {distancia:.2f}")

if __name__ == "__main__":
    print(" CLASE 5 - ALGEBRA LINEAL CON NUMPY")
    print("Jonathan Ruiz Ordoñez - 29 Oct 2024")
    print("=" * 60)
    
    vectores = demostrar_vectores()
    matrices = demostrar_matrices()
    comparar_python_numpy()
    ejercicios_practicos()
    
    print("\n" + "=" * 50)
    print(" CLASE 5 COMPLETADA - FUNDAMENTOS DE ALGEBRA LINEAL")
    print("=" * 50)
    print(" Conceptos dominados:")
    print("    Vectores y operaciones vectoriales")
    print("    Matrices y operaciones matriciales")
    print("    Producto punto y normas")
    print("    Matriz identidad y transpuesta")
    print("    Diferencias Python vs NumPy")

# En Git Bash, ejecuta:
cp "C:/Users/j_rui/OneDrive/Documentos/De Cero a Ciencia de Datos/Clase 5/Algebra_Lineal.ipynb" "clase-5-algebra-lineal-numpy/ejercicios-clase-5.ipynb"
# Entrar a la carpeta de clase 5
cd clase-5-algebra-lineal-numpy

# Ver los archivos
ls -la
fwd
exit()
exit
cwd
pwd
exit


quit()
