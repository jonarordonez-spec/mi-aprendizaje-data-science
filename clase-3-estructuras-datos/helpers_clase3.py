"""
Script de apoyo - Clase 3: Estructuras de Datos y Control en Python
Autor: Jonathan Ruiz Ordoñez
Fecha: 29 de Octubre 2024
Descripción: Demostración de conceptos aprendidos en la tercera clase de Data Science
"""

def demostrar_variables_atomicas():
    """Demuestra los tipos de datos atómicos en Python"""
    print("=" * 50)
    print("🔢 VARIABLES Y DATOS ATÓMICOS")
    print("=" * 50)
    
    # Variables atómicas
    entero = 15
    flotante = 15.3
    cadena = "texto"
    booleano = True
    
    print(f"Entero: {entero} (tipo: {type(entero)})")
    print(f"Flotante: {flotante} (tipo: {type(flotante)})")
    print(f"Cadena: '{cadena}' (tipo: {type(cadena)})")
    print(f"Booleano: {booleano} (tipo: {type(booleano)})")
    
    # Operaciones con variables
    suma = entero + flotante
    print(f"\nSuma de {entero} + {flotante} = {suma}")
    
    return entero, flotante, cadena, booleano

def demostrar_listas():
    """Demuestra el uso de listas en Python"""
    print("\n" + "=" * 50)
    print("📋 LISTAS EN PYTHON")
    print("=" * 50)
    
    # Crear listas
    nombres = ["Noemi", "Jonathan", "Melissa", "Edgar"]
    numeros = [1, 2, 3, 4, 5, 6, 7]
    combinada = ["hola", 12, [1, 2]]
    
    print(f"Lista de nombres: {nombres}")
    print(f"Lista de números: {numeros}")
    print(f"Lista combinada: {combinada}")
    
    # Operaciones con listas
    numeros.append(8)  # Agregar al final
    numeros.insert(0, 0)  # Insertar en posición
    numeros.remove(3)  # Remover elemento
    
    print(f"\nLista modificada: {numeros}")
    print(f"Primer elemento: {nombres[0]}")
    print(f"Último elemento: {nombres[-1]}")
    print(f"Longitud de la lista: {len(nombres)}")
    
    return nombres, numeros, combinada

def demostrar_condicionales():
    """Demuestra estructuras condicionales if-elif-else"""
    print("\n" + "=" * 50)
    print("🎯 ESTRUCTURAS CONDICIONALES")
    print("=" * 50)
    
    edad = 18
    
    # Condicional básico
    if edad >= 18:
        print("✅ Eres mayor de edad")
        años_21 = 21 - edad
        print(f"Te faltan {años_21} años para cumplir 21 años")
    else:
        print("❌ Eres menor de edad")
        años_21 = 21 - edad
        print(f"Te faltan {años_21} años para cumplir 21 años")
    
    # Condicional con input (simulado)
    print("\n--- Ejemplo con Input ---")
    edad_usuario = 20  # Simulando input
    if edad_usuario >= 18:
        print("✅ Puedes aprender ciencia de datos sin permiso de tus papás")
    else:
        print("🎉 Que chido que empieces joven")
    
    return edad

def demostrar_bucles():
    """Demuestra bucles for y while"""
    print("\n" + "=" * 50)
    print("🔄 ESTRUCTURAS DE REPETICIÓN")
    print("=" * 50)
    
    # Bucle for
    print("--- Bucle FOR ---")
    lenguajes = ["Python", "R", "SQL", "Julia", "Scala"]
    for lenguaje in lenguajes:
        print(f"💻 Uno de los lenguajes más usados es: {lenguaje}")
    
    # Bucle while
    print("\n--- Bucle WHILE ---")
    dias_estudio = 0
    while dias_estudio < 3:
        print(f"📚 Estudia un poco más, Día {dias_estudio + 1}")
        dias_estudio += 1
    print("🎊 Bien hecho, has estudiado al menos 3 días esta semana")
    
    return lenguajes

def demostrar_diccionarios():
    """Demuestra el uso de diccionarios"""
    print("\n" + "=" * 50)
    print("📖 DICCIONARIOS EN PYTHON")
    print("=" * 50)
    
    # Crear diccionario
    mi_dict = {
        "nombre": "Python", 
        "version": 3.12, 
        "activo": True,
        "año": 2024
    }
    
    print(f"Diccionario completo: {mi_dict}")
    print(f"Nombre del lenguaje: {mi_dict['nombre']}")
    print(f"Versión: {mi_dict['version']}")
    
    # Recorrer diccionario
    print("\n--- Recorriendo diccionario ---")
    for clave, valor in mi_dict.items():
        print(f"🔑 {clave}: {valor}")
    
    return mi_dict

def demostrar_funciones():
    """Demuestra la creación y uso de funciones"""
    print("\n" + "=" * 50)
    print("⚙️ FUNCIONES EN PYTHON")
    print("=" * 50)
    
    # Función simple
    def saludar():
        print("👋 Hola, bienvenida al mundo de la ciencia de datos")
    
    # Función con parámetros
    def saludar_persona(nombre):
        print(f"🎉 Hola {nombre}, bienvenido al curso")
    
    # Función con return
    def sumar(a, b):
        resultado = a + b
        return resultado
    
    # Ejecutar funciones
    saludar()
    saludar_persona("Jonathan")
    resultado_suma = sumar(10, 5)
    print(f"➗ Resultado de la suma: {resultado_suma}")
    
    return saludar, saludar_persona, sumar

if __name__ == "__main__":
    print("🚀 INICIANDO CLASE 3 - ESTRUCTURAS DE DATOS Y CONTROL\n")
    print("Autor: Jonathan Ruiz Ordoñez")
    print("=" * 60)
    
    # Ejecutar todas las demostraciones
    variables = demostrar_variables_atomicas()
    listas = demostrar_listas()
    condicionales = demostrar_condicionales()
    bucles = demostrar_bucles()
    diccionarios = demostrar_diccionarios()
    funciones = demostrar_funciones()
    
    print("\n" + "=" * 50)
    print("✅ CLASE 3 COMPLETADA EXITOSAMENTE")
    print("=" * 50)
    print("🎯 Conceptos aprendidos:")
    print("   • Variables y tipos de datos")
    print("   • Listas y operaciones")
    print("   • Estructuras condicionales")
    print("   • Bucles for y while")
    print("   • Diccionarios")
    print("   • Funciones y parámetros")
    print("\n📚 Revisa el notebook 'ejercicios-clase-3.ipynb' para más ejercicios")
