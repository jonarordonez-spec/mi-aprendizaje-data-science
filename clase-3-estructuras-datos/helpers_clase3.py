"""
Script de apoyo - Clase 3: Estructuras de Datos en Python
Autor: Jonathan Ruiz Ordoñez
Fecha: [Fecha de tu clase 3]
Descripción: Demostración de estructuras de datos aprendidas en la tercera clase
"""

def demostrar_listas():
    """Demuestra el uso de listas en Python"""
    print("=" * 50)
    print("📋 LISTAS EN PYTHON")
    print("=" * 50)
    
    # Crear una lista
    frutas = ["manzana", "banana", "naranja", "uva"]
    print(f"Lista original: {frutas}")
    
    # Operaciones comunes con listas
    frutas.append("mango")  # Agregar elemento
    frutas.insert(1, "fresa")  # Insertar en posición
    frutas.remove("banana")  # Remover elemento
    
    print(f"Lista modificada: {frutas}")
    print(f"Primer elemento: {frutas[0]}")
    print(f"Último elemento: {frutas[-1]}")
    print(f"Longitud de la lista: {len(frutas)}")
    
    return frutas

def demostrar_diccionarios():
    """Demuestra el uso de diccionarios en Python"""
    print("\n" + "=" * 50)
    print("📖 DICCIONARIOS EN PYTHON")
    print("=" * 50)
    
    # Crear un diccionario de estudiante
    estudiante = {
        "nombre": "Jonathan Ruiz",
        "edad": 25,
        "curso": "Data Science",
        "habilidades": ["Python", "Pandas", "SQL"],
        "proyectos_completados": 3
    }
    
    print(f"Diccionario del estudiante: {estudiante}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Habilidades: {', '.join(estudiante['habilidades'])}")
    
    # Agregar nueva clave
    estudiante["nuevo_proyecto"] = "Análisis de datos"
    print(f"Proyecto agregado: {estudiante['nuevo_proyecto']}")
    
    return estudiante

def demostrar_tuplas():
    """Demuestra el uso de tuplas en Python"""
    print("\n" + "=" * 50)
    print("📦 TUPLAS EN PYTHON")
    print("=" * 50)
    
    # Crear una tupla (inmutable)
    coordenadas = (40.7128, -74.0060)
    colores_rgb = (255, 128, 0)
    
    print(f"Coordenadas NYC: {coordenadas}")
    print(f"Color RGB naranja: {colores_rgb}")
    print(f"Latitud: {coordenadas[0]}")
    print(f"Longitud: {coordenadas[1]}")
    
    return coordenadas, colores_rgb

def operaciones_avanzadas():
    """Demuestra operaciones avanzadas con estructuras de datos"""
    print("\n" + "=" * 50)
    print("🚀 OPERACIONES AVANZADAS")
    print("=" * 50)
    
    # Comprensión de listas
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]
    
    print(f"Números originales: {numeros}")
    print(f"Cuadrados de números pares: {cuadrados_pares}")
    
    # Diccionario con comprensión
    cubos = {x: x**3 for x in range(1, 6)}
    print(f"Cubos del 1 al 5: {cubos}")
    
    return cuadrados_pares, cubos

if __name__ == "__main__":
    print("🚀 INICIANDO CLASE 3 - ESTRUCTURAS DE DATOS\n")
    print("Autor: Jonathan Ruiz Ordoñez")
    print("=" * 60)
    
    listas = demostrar_listas()
    diccionarios = demostrar_diccionarios()
    tuplas = demostrar_tuplas()
    avanzadas = operaciones_avanzadas()
    
    print("\n" + "=" * 50)
    print("✅ DEMOSTRACIÓN COMPLETADA")
    print("=" * 50)
    print("Estructuras creadas exitosamente:")
    print(f"- Lista: {len(listas)} elementos")
    print(f"- Diccionario: {len(diccionarios)} claves")
    print(f"- Tupla: {len(tuplas)} elementos")
