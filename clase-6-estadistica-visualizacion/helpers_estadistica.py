"""
Helpers para Estadística Descriptiva - Clase 6
Funciones útiles para análisis estadístico y visualización
Autor: Jonathan Ruiz Ordoñez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def analisis_estadistico_completo(datos, nombre_columna=None):
    """
    Realiza análisis estadístico completo de un conjunto de datos
    
    Parameters:
    datos: array-like o Series de pandas
    nombre_columna: str, nombre de la columna (opcional)
    """
    print("=" * 60)
    print("📊 ANÁLISIS ESTADÍSTICO COMPLETO")
    print("=" * 60)
    
    # Convertir a numpy array si es necesario
    if hasattr(datos, 'values'):
        datos_array = datos.values
    else:
        datos_array = np.array(datos)
    
    # Medidas de tendencia central
    media = np.mean(datos_array)
    mediana = np.median(datos_array)
    moda = stats.mode(datos_array)
    
    # Medidas de dispersión
    varianza = np.var(datos_array)
    desviacion_estandar = np.std(datos_array)
    rango = np.max(datos_array) - np.min(datos_array)
    
    # Cuantiles
    cuartiles = np.percentile(datos_array, [25, 50, 75])
    percentiles = np.percentile(datos_array, [10, 25, 50, 75, 90])
    
    # Mostrar resultados
    if nombre_columna:
        print(f"Variable: {nombre_columna}")
    
    print(f"\n🔹 MEDIDAS DE TENDENCIA CENTRAL:")
    print(f"   Media: {media:.2f}")
    print(f"   Mediana: {mediana:.2f}")
    print(f"   Moda: {moda.mode[0]} (frecuencia: {moda.count[0]})")
    
    print(f"\n🔹 MEDIDAS DE DISPERSIÓN:")
    print(f"   Varianza: {varianza:.2f}")
    print(f"   Desviación Estándar: {desviacion_estandar:.2f}")
    print(f"   Rango: {rango:.2f}")
    
    print(f"\n🔹 CUANTILES:")
    print(f"   Q1 (25%): {cuartiles[0]:.2f}")
    print(f"   Q2/Mediana (50%): {cuartiles[1]:.2f}")
    print(f"   Q3 (75%): {cuartiles[2]:.2f}")
    print(f"   Percentil 10: {percentiles[0]:.2f}")
    print(f"   Percentil 90: {percentiles[4]:.2f}")
    
    print(f"\n📈 RESUMEN:")
    print(f"   Tamaño de muestra: {len(datos_array)}")
    print(f"   Valor mínimo: {np.min(datos_array):.2f}")
    print(f"   Valor máximo: {np.max(datos_array):.2f}")
    
    return {
        'media': media,
        'mediana': mediana,
        'moda': moda.mode[0],
        'varianza': varianza,
        'desviacion_estandar': desviacion_estandar,
        'rango': rango,
        'cuartiles': cuartiles
    }

def crear_visualizacion_estadistica(datos, titulo="Distribución de Datos"):
    """
    Crea visualización completa para análisis estadístico
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Histograma
    ax1.hist(datos, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
    ax1.axvline(np.mean(datos), color='red', linestyle='--', label=f'Media: {np.mean(datos):.2f}')
    ax1.axvline(np.median(datos), color='green', linestyle='--', label=f'Mediana: {np.median(datos):.2f}')
    ax1.set_title('Histograma y Medidas de Tendencia Central')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Boxplot
    ax2.boxplot(datos, vert=True, patch_artist=True)
    ax2.set_title('Diagrama de Caja (Boxplot)')
    ax2.set_ylabel('Valores')
    ax2.grid(True, alpha=0.3)
    
    # Gráfico de densidad
    from scipy.stats import gaussian_kde
    densidad = gaussian_kde(datos)
    x_range = np.linspace(min(datos), max(datos), 100)
    ax3.plot(x_range, densidad(x_range), color='purple', linewidth=2)
    ax3.fill_between(x_range, densidad(x_range), alpha=0.3, color='purple')
    ax3.set_title('Función de Densidad de Probabilidad')
    ax3.grid(True, alpha=0.3)
    
    # Gráfico de cuantiles
    ax4.scatter(range(len(datos)), np.sort(datos), alpha=0.6, color='orange')
    ax4.set_title('Gráfico de Cuantiles')
    ax4.set_xlabel('Orden')
    ax4.set_ylabel('Valores Ordenados')
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle(titulo, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('analisis_estadistico_completo.png', dpi=300, bbox_inches='tight')
    plt.show()

def demostrar_algebra_lineal():
    """
    Demuestra conceptos de álgebra lineal aprendidos
    """
    print("\n" + "=" * 50)
    print("🧮 ÁLGEBRA LINEAL - OPERACIONES BÁSICAS")
    print("=" * 50)
    
    # Vectores
    v1 = np.array([2, 4, 6])
    v2 = np.array([1, 3, 5])
    
    print("Vectores:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    # Operaciones vectoriales
    print(f"\nOperaciones Vectoriales:")
    print(f"Suma: v1 + v2 = {v1 + v2}")
    print(f"Resta: v1 - v2 = {v1 - v2}")
    print(f"Multiplicación por escalar: 2 * v1 = {2 * v1}")
    print(f"Producto punto: v1 · v2 = {np.dot(v1, v2)}")
    print(f"Norma de v1: ||v1|| = {np.linalg.norm(v1):.2f}")
    
    # Matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"\nMatrices:")
    print(f"A = \n{A}")
    print(f"B = \n{B}")
    print(f"Multiplicación A x B = \n{A @ B}")
    print(f"Determinante de A: {np.linalg.det(A):.2f}")
    print(f"Matriz inversa de A: \n{np.linalg.inv(A)}")

if __name__ == "__main__":
    # Ejemplo de uso
    print("🚀 CLASE 6 - ESTADÍSTICA Y VISUALIZACIÓN")
    
    # Datos de ejemplo
    datos_ejemplo = np.random.normal(100, 15, 1000)  # Distribución normal
    
    # Análisis estadístico
    resultados = analisis_estadistico_completo(datos_ejemplo, "Ejemplo - Puntajes")
    
    # Visualización
    crear_visualizacion_estadistica(datos_ejemplo, "Análisis Estadístico Completo")
    
    # Álgebra lineal
    demostrar_algebra_lineal()
    
    print("\n✅ Análisis completado - Revisa el archivo 'analisis_estadistico_completo.png'")
