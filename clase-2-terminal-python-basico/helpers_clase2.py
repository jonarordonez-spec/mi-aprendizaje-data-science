"""
Script de apoyo - Clase 2: Terminal y Python Básico
Autor: Jonathan Ruiz Ordoñez
Fecha: 28 de Octubre 2024
Descripción: Demostración de conceptos aprendidos en la segunda clase de Data Science
"""

def mostrar_info_estudiante():
    """Muestra la información del estudiante"""
    print("=" * 60)
    print("INFORMACIÓN DEL ESTUDIANTE")
    print("=" * 60)
    
    info_estudiante = {
        "Nombre": "Jonathan Ruiz Ordoñez",
        "Curso": "Data Science - De Cero a Ciencia de Datos", 
        "Clase": "2 - Terminal y Python Básico",
        "Fecha": "28 de Octubre 2024",
        "Objetivo": "Aprender Git/GitHub y construir portafolio profesional"
    }
    
    for clave, valor in info_estudiante.items():
        print(f"📍 {clave}: {valor}")
    
    print("=" * 60)
    return info_estudiante

def demostrar_conceptos_clase():
    """Demuestra los conceptos aprendidos en la clase 2"""
    print("\n" + "=" * 50)
    print("CONCEPTOS APRENDIDOS - CLASE 2")
    print("=" * 50)
    
    conceptos = {
        "Terminal/CMD": "Herramienta para comunicarse con el OS via comandos",
        "Script": "Archivo con comandos para automatizar tareas", 
        "IDE": "Entorno para escribir, ejecutar y debuggear código",
        "Jupyter Notebook": "IDE interactivo para análisis de datos",
        "Git": "Sistema de control de versiones",
        "GitHub": "Plataforma para alojar y colaborar en proyectos",
        "Commit": "Guardado de cambios en el historial de Git",
        "Push": "Subir cambios locales al repositorio remoto"
    }
    
    for i, (concepto, descripcion) in enumerate(conceptos.items(), 1):
        print(f"{i}. 🧩 {concepto}: {descripcion}")
    
    return conceptos

def operaciones_matematicas():
    """Ejemplos de operaciones Python aprendidas"""
    print("\n" + "=" * 40)
    print("OPERACIONES MATEMÁTICAS EN PYTHON")
    print("=" * 40)
    
    a, b = 20, 4
    operaciones = {
        "Suma": f"{a} + {b} = {a + b}",
        "Resta": f"{a} - {b} = {a - b}", 
        "Multiplicación": f"{a} * {b} = {a * b}",
        "División": f"{a} / {b} = {a / b:.2f}",
        "División Entera": f"{a} // {b} = {a // b}",
        "Módulo": f"{a} % {b} = {a % b}",
        "Potencia": f"{a} ** {b} = {a ** b}"
    }
    
    for nombre, resultado in operaciones.items():
        print(f"➡️ {resultado}")
    
    return operaciones

def mostrar_proximo_paso():
    """Muestra los próximos objetivos de aprendizaje"""
    print("\n" + "=" * 50)
    print("PRÓXIMOS OBJETIVOS DE APRENDIZAJE")
    print("=" * 50)
    
    objetivos = [
        "Estructuras de datos en Python (listas, diccionarios)",
        "Introducción a Pandas para análisis de datos", 
        "Visualización de datos con Matplotlib y Seaborn",
        "Modelos básicos de Machine Learning",
        "Continuar construciendo mi portafolio en GitHub"
    ]
    
    for objetivo in objetivos:
        print(f"✅ {objetivo}")

if __name__ == "__main__":
    print("INICIANDO DEMOSTRACIÓN - JONATHAN RUIZ ORDOÑEZ\n")
    mostrar_info_estudiante()
    demostrar_conceptos_clase() 
    operaciones_matematicas()
    mostrar_proximo_paso()
