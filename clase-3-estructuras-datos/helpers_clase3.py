"""
Script de apoyo - Clase 3: Estructuras de Datos y Control en Python
Autor: Jonathan Ruiz Ordoñez  
Fecha: 29 de Octubre 2024
Descripción: Ejercicios prácticos de mi tercera clase de Data Science
Contiene mi código real de práctica
"""

def mis_variables():
    """Mis ejercicios con variables atómicas"""
    print("=== MIS VARIABLES ===")
    
    entero = 15
    flotante = 15.3
    cadena = "texto"
    booleano = True
    
    print(f"Entero: {entero}")
    print(f"Flotante: {flotante}") 
    print(f"Cadena: {cadena}")
    print(f"Booleano: {booleano}")
    
    # Mi operación
    suma = entero + flotante
    print(f"Suma: {entero} + {flotante} = {suma}")
    print(f"Tipo de suma: {type(suma)}")

def mis_listas():
    """Mis ejercicios con listas"""
    print("\n=== MIS LISTAS ===")
    
    nombres = ["Noemi", "Jonathan", "Melissa", "Edgar"]
    numeros = [1, 2, 3, 4, 5, 6, 7]
    combi = ["hola", 12, [1, 2]]
    
    print("Lista nombres:", nombres)
    print("Lista números:", numeros) 
    print("Lista combinada:", combi)
    
    # Mis operaciones con listas
    numeros.append(8)
    print("Después de append(8):", numeros)
    
    numeros.remove(3)
    print("Después de remove(3):", numeros)

def mi_funcion_gatito():
    """Mi función de gatito de la clase"""
    print("\n=== MI FUNCIÓN GATITO ===")
    
    nombre = "Panchito"
    edad = 4
    personalidad = "jugueton"
    
    def gatite(name, age, style):
        print(f"Le gatite {name} tiene {age} años y su personalidad es {style}")
    
    gatite(nombre, edad, personalidad)
    gatite("polo", 7, "cariñoso")

def mis_condicionales():
    """Mis ejercicios con if-else"""
    print("\n=== MIS CONDICIONALES ===")
    
    edad = 18
    
    if edad >= 18:
        print("Eres mayor de edad")
        años_para_cumplir_21 = 21 - edad
        print(f"Te faltan {años_para_cumplir_21} años para cumplir 21 años")
    else:
        print("Eres menor de edad")
        años_para_cumplir_21 = 21 - edad  
        print(f"Te faltan {años_para_cumplir_21} años para cumplir 21 años")
    
    # Mi ejemplo de hora de comida
    hora_de_comida = 3
    contacto = 4
    
    if contacto != hora_de_comida:
        print("Si te puedo atender")
    else:
        print("No te puedo atender")

def mis_bucles():
    """Mis ejercicios con bucles"""
    print("\n=== MIS BUCLES ===")
    
    nombres = ["Noemi", "Jonathan", "Melissa", "Edgar"]
    lenguajes = ["Python", "R", "SQL", "Julia", "Scala"]
    
    print("--- Mi bucle for con nombres ---")
    for i in nombres:
        print(i)
    
    print("\n--- Mi bucle for con lenguajes ---") 
    for lenguaje in lenguajes:
        print(f"Uno de los lenguajes más usados es: {lenguaje}")
    
    print("\n--- Mi bucle while ---")
    x = 0
    while x < 5:
        print(x)
        x += 1

def mis_diccionarios():
    """Mis ejercicios con diccionarios"""
    print("\n=== MIS DICCIONARIOS ===")
    
    mi_dict = {"nombre": "Python", "version": 3.12, "activo": True}
    print("Mi diccionario:", mi_dict)
    
    # Agregar nueva clave
    mi_dict["año"] = 2024
    print("Después de agregar año:", mi_dict)
    
    print("\n--- Recorriendo mi diccionario ---")
    for key, value in mi_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("🚀 MI CLASE 3 - EJERCICIOS PRÁCTICOS")
    print("Jonathan Ruiz Ordoñez - 29 Oct 2024")
    print("=" * 50)
    
    mis_variables()
    mis_listas() 
    mi_funcion_gatito()
    mis_condicionales()
    mis_bucles()
    mis_diccionarios()
    
    print("\n" + "=" * 50)
    print("✅ EJERCICIOS COMPLETADOS")
    print("Todos estos conceptos los practiqué en mi notebook de clase")
