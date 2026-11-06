"""
Katas de Python — Pablo Tomé Manzano
Colección de 40 ejercicios resueltos con tipado estricto, docstrings y buenas prácticas.
"""

# =============================================================================
# 1. Frecuencia de caracteres en una cadena
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
# =============================================================================

def frecuencia_caracteres(texto: str) -> dict:
    """Calcula la frecuencia de cada letra en una cadena de texto, omitiendo espacios."""
    texto_lower = texto.lower()
    dict_letras = {}

    for letra in texto_lower:
        if letra == " ":
            continue
        elif letra not in dict_letras:
            dict_letras[letra] = 1
        else:
            dict_letras[letra] += 1
            
    return dict_letras

# Prueba del ejercicio
cadena_prueba = "Katas de Python en 2DAW"
print(frecuencia_caracteres(cadena_prueba))

# =============================================================================
# 2. Doble de cada valor con map()
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
# =============================================================================

def doble_valor(lista: list[int | float]) -> list[int | float]:
    """Devuelve una nueva lista con el doble de cada número usando map()."""
    return list(map(lambda x: x * 2, lista))

# Prueba del ejercicio
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(doble_valor(numeros))

# =============================================================================
# 3. Filtrar palabras que contienen una subcadena objetivo
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# =============================================================================

def buscar_palabra(lista: list[str], palabra_objetivo: str) -> list[str]:
    """Devuelve las palabras de una lista que contienen la subcadena objetivo."""
    resultado = []
    for palabra in lista:
        if palabra_objetivo.lower() in palabra.lower():
            resultado.append(palabra)
    return resultado

# Prueba del ejercicio
palabras = ['leon', 'camion', 'conductor', 'cuidador', 'explosion', 'reventon', 'cuchara', 'pedro']
print(buscar_palabra(palabras, 'on'))

# =============================================================================
# 4. Diferencia entre valores de dos listas con map() y lambda
# Genera una función que calcule la diferencia entre los valores de dos listas elemento a elemento. Usa la función map().
# =============================================================================

def diferencia_valor(lista1: list[int | float], lista2: list[int | float]) -> list[int | float]:
    """Calcula la diferencia elemento a elemento de dos listas usando map() y lambda."""
    return list(map(lambda x, y: x - y, lista1, lista2))

# Prueba del ejercicio
l1 = [10, 20, 30, 40]
l2 = [3, 5, 10, 15]
print(diferencia_valor(l1, l2))

# =============================================================================
# 5. Diferencia entre dos listas importando el módulo operator
# Calcula la diferencia entre los valores de dos listas utilizando el operador de sustracción sub del módulo operator.
# =============================================================================

from operator import sub

def diferencia_listas(lista1: list[int | float], lista2: list[int | float]) -> list[int | float]:
    """Calcula la diferencia elemento a elemento de dos listas usando operator.sub y map()."""
    return list(map(sub, lista1, lista2))

# Prueba del ejercicio
l1 = [10, 20, 30, 40]
l2 = [3, 5, 10, 15]
print(diferencia_listas(l1, l2))

# =============================================================================
# 6. Cálculo de nota media y estado de aprobación
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será 'aprobado'; de lo contrario, 'suspenso'. La función debe devolver una tupla que contenga la media y el estado.
# =============================================================================

def calcular_media(lista_notas: list[float], nota_aprobado: float = 5.0) -> tuple[float, str]:
    """Calcula la media de una lista de notas y retorna una tupla (media, estado)."""
    media = sum(lista_notas) / len(lista_notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (round(media, 2), estado)

# Prueba del ejercicio
notas_alumno1 = [4, 6, 5, 7, 3]
media1, estado1 = calcular_media(notas_alumno1)
print(f"Media: {media1}, Estado: {estado1}")

# =============================================================================
# 7. División de dos números con manejo de excepciones
# Escribe un programa que pida dos números e intente dividirlos. Si se ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones adecuadamente y muestra un mensaje indicando si la división fue exitosa o no.
# =============================================================================

def dividir_numeros(num1_val=10, num2_val=2):
    """Realiza la división entre dos números capturando ValueError y ZeroDivisionError."""
    try:
        num1 = float(num1_val)
        num2 = float(num2_val)
        resultado = num1 / num2
    except ValueError:
        print("❌ Error: Debes ingresar valores numéricos válidos.")
        print("La división NO fue exitosa.")
        return None
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir entre cero.")
        print("La división NO fue exitosa.")
        return None
    else:
        print(f"✅ Éxito: El resultado de {num1} / {num2} es {resultado}")
        print("La división fue exitosa.")
        return resultado

# Pruebas del ejercicio
print("--- Caso 1: División exitosa ---")
dividir_numeros(10, 2)

print()
print("--- Caso 2: División entre cero ---")
dividir_numeros(10, 0)

# =============================================================================
# 8. Conversión de lista de tuplas a lista de strings con map()
# Genera una función que convierta una lista de tuplas a una lista de strings uniendo sus elementos. Usa la función map().
# =============================================================================

def conversor_tupla_string(tuplas: list[tuple[str, ...]]) -> list[str]:
    """Une las cadenas contenidas en cada tupla formando un string único por elemento."""
    return list(map(lambda t: " ".join(t), tuplas))

# Prueba del ejercicio
tuplas = [('Hola', 'Mundo'), ('Python', 'es', 'genial'), ('Katas', '2026')]
print(conversor_tupla_string(tuplas))

# =============================================================================
# 9. Filtrar mascotas excluyendo las prohibidas con filter()
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España (['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']). Usa la función filter().
# =============================================================================

def filtrar_mascotas(lista_mascotas: list[str]) -> list[str]:
    """Filtra una lista de mascotas excluyendo las prohibidas por ley."""
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

# Prueba del ejercicio
mis_mascotas = ["Perro", "Tigre", "Gato", "Mapache", "Hámster", "Oso"]
print(filtrar_mascotas(mis_mascotas))

# =============================================================================
# 10. Promedio de lista con excepción personalizada si está vacía
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
# =============================================================================

class ListaVaciaError(Exception):
    """Excepción lanzada cuando la lista de números está vacía."""
    pass

def calculo_promedio(lista_numeros: list[float]) -> float:
    """Calcula el promedio de una lista o lanza ListaVaciaError si está vacía."""
    if not lista_numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(lista_numeros) / len(lista_numeros)

# Pruebas del ejercicio
try:
    print("Promedio lista normal:", calculo_promedio([10, 20, 30, 40]))
    calculo_promedio([])
except ListaVaciaError as e:
    print(f"Excepción capturada con éxito: {e}")

# =============================================================================
# 11. Solicitud de edad y validación de rango con excepciones
# Escribe un programa que solicite la edad al usuario. Si ingresa un valor no numérico o fuera del rango esperado (0-120), maneja las excepciones adecuadamente.
# =============================================================================

class EdadFueraDeRango(Exception):
    """Excepción para indicar que la edad introducida no se encuentra entre 0 y 120."""
    pass

def solicitar_edad(edad_entrada=None):
    """Valida que la edad sea un entero entre 0 y 120 años."""
    try:
        entrada = edad_entrada if edad_entrada is not None else input("Por favor, introduce tu edad: ")
        edad = int(entrada)
        
        if edad < 0 or edad > 120:
            raise EdadFueraDeRango(f"La edad {edad} está fuera del rango permitido (0-120).")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido.")
        return None
    except EdadFueraDeRango as e:
        print(f"❌ Excepción capturada: {e}")
        return None
    else:
        print(f"✅ Edad registrada correctamente ({edad} años).")
        return edad

# Pruebas del ejercicio
solicitar_edad(25)
solicitar_edad(135)
solicitar_edad("veinte")

# =============================================================================
# 12. Longitud de cada palabra de una frase con map()
# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
# =============================================================================

def longitud_palabras(frase: str) -> list[int]:
    """Calcula la longitud de cada palabra de una frase usando map()."""
    palabras = frase.split()
    return list(map(len, palabras))

# Prueba del ejercicio
frase_ejemplo = "Desarrollo de aplicaciones web con Python"
print(longitud_palabras(frase_ejemplo))

# =============================================================================
# 13. Tuplas de mayúsculas y minúsculas sin repetir caracteres
# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
# =============================================================================

def map_mayus_minus(caracteres: list[str]) -> list[tuple[str, str]]:
    """Devuelve tuplas (MAYÚSCULA, minúscula) de caracteres únicos usando map()."""
    unicos = sorted(set(c.lower() for c in caracteres))
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

# Prueba del ejercicio
letras = ["a", "b", "c", "a", "B", "C", "d"]
print(map_mayus_minus(letras))

# =============================================================================
# 14. Filtrar palabras por letra inicial con filter()
# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
# =============================================================================

def palabras_por_letra(lista_palabras: list[str], letra: str) -> list[str]:
    """Filtra palabras que empiezan por la letra dada (insensible a mayúsculas/minúsculas)."""
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista_palabras))

# Prueba del ejercicio
palabras = ["perro", "gato", "pájaro", "pez", "ratón", "Pantera"]
print(palabras_por_letra(palabras, "p"))

# =============================================================================
# 15. Función lambda para sumar 3 a cada número de una lista
# Crea una función lambda que sume 3 a cada número de una lista dada con map().
# =============================================================================

def sumar_tres(lista_numeros: list[int | float]) -> list[int | float]:
    """Suma 3 a cada elemento de una lista mediante lambda y map()."""
    return list(map(lambda x: x + 3, lista_numeros))

# Prueba del ejercicio
numeros = [1, 5, 10, 15, 20]
print(sumar_tres(numeros))

# =============================================================================
# 16. Filtrar palabras más largas que n caracteres
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
# =============================================================================

def palabras_mas_largas(texto: str, n: int) -> list[str]:
    """Filtra las palabras del texto cuya longitud sea estrictamente mayor que n."""
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Prueba del ejercicio
texto_muestra = "El veloz murciélago hindú comía feliz cardillo y kiwi"
print(palabras_mas_largas(texto_muestra, 5))

# =============================================================================
# 17. Convertir lista de dígitos a número entero con reduce()
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5, 7, 2] corresponde al número 572. Usa la función reduce().
# =============================================================================

from functools import reduce

def digitos_a_numero(digitos: list[int]) -> int:
    """Convierte una lista de dígitos en el número decimal equivalente usando reduce()."""
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

# Prueba del ejercicio
lista_digitos = [5, 7, 2]
print(digitos_a_numero(lista_digitos))

# =============================================================================
# 18. Filtrar estudiantes con calificación sobresaliente (>= 90)
# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
# =============================================================================

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Carlos", "edad": 22, "calificacion": 92},
    {"nombre": "Beatriz", "edad": 21, "calificacion": 78},
    {"nombre": "David", "edad": 23, "calificacion": 95},
    {"nombre": "Elena", "edad": 19, "calificacion": 89}
]

estudiantes_sobresalientes = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))
print(estudiantes_sobresalientes)

# =============================================================================
# 19. Filtrar números impares de una lista con filter()
# Crea una función lambda que filtre los números impares de una lista dada con filter().
# =============================================================================

def filtro_impares(lista_numeros: list[int]) -> list[int]:
    """Filtra y devuelve exclusivamente los números impares usando filter()."""
    return list(filter(lambda x: x % 2 != 0, lista_numeros))

# Prueba del ejercicio
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtro_impares(numeros))

# =============================================================================
# 20. Filtrar solo elementos enteros con type(x) is int
# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter() verificando con type(x) is int para excluir booleanos.
# =============================================================================

def buscar_enteros(lista_mixta: list) -> list[int]:
    """Devuelve únicamente los enteros excluyendo booleanos usando type(x) is int."""
    return list(filter(lambda x: type(x) is int, lista_mixta))

# Prueba del ejercicio (incluye booleano True para verificar que no pasa)
lista_elementos = [10, "hola", 25, "python", 100, "katas", True]
print(buscar_enteros(lista_elementos))

# =============================================================================
# 21. Cálculo del cubo de un número con función lambda
# Crea una función que calcule el cubo de un número dado mediante una función lambda.
# =============================================================================

cubo_numero = lambda x: x ** 3

# Pruebas del ejercicio
print("Cubo de 3:", cubo_numero(3))
print("Cubo de 5:", cubo_numero(5))

# =============================================================================
# 22. Producto total de los valores de una lista con reduce()
# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
# =============================================================================

from functools import reduce

def producto_total(numeros: list[int | float]) -> int | float:
    """Calcula la multiplicación acumulada de todos los elementos con reduce()."""
    return reduce(lambda acumulado, x: acumulado * x, numeros)

# Prueba del ejercicio
lista_numeros = [2, 3, 4, 5]
print(producto_total(lista_numeros))

# =============================================================================
# 23. Concatenación de una lista de palabras con reduce()
# Concatena una lista de palabras unidas por un espacio. Usa la función reduce().
# =============================================================================

from functools import reduce

def concatenar_palabras(lista_palabras: list[str]) -> str:
    """Concatena palabras de una lista separándolas por espacios usando reduce()."""
    return reduce(lambda p1, p2: p1 + " " + p2, lista_palabras)

# Prueba del ejercicio
palabras = ["Hola", "mundo", "desde", "Python", "Katas"]
print(concatenar_palabras(palabras))

# =============================================================================
# 24. Diferencia acumulada total en una lista con reduce()
# Calcula la diferencia total en los valores de una lista restando secuencialmente. Usa la función reduce().
# =============================================================================

from functools import reduce

def diferencia_total(numeros: list[int | float]) -> int | float:
    """Resta secuencialmente todos los números de la lista con reduce()."""
    return reduce(lambda x, y: x - y, numeros)

# Prueba del ejercicio
valores = [100, 20, 10, 5]
print(diferencia_total(valores))

# =============================================================================
# 25. Conteo del número de caracteres en una cadena
# Crea una función que cuente el número total de caracteres en una cadena de texto dada.
# =============================================================================

def contar_caracteres(texto: str) -> int:
    """Cuenta el número total de caracteres de la cadena."""
    return len(texto)

# Prueba del ejercicio
cadena = "Katas de Python 2026"
print(contar_caracteres(cadena))

# =============================================================================
# 26. Resto de la división entre dos números con lambda
# Crea una función lambda que calcule el resto de la división (módulo) entre dos números dados.
# =============================================================================

resto_division = lambda a, b: a % b

# Pruebas del ejercicio
print("17 % 5 =", resto_division(17, 5))
print("20 % 4 =", resto_division(20, 4))

# =============================================================================
# 27. Cálculo del promedio de una lista de números
# Crea una función que calcule el promedio de una lista de números.
# =============================================================================

def promedio_lista(numeros: list[float]) -> float:
    """Calcula la media aritmética de una lista de valores numéricos."""
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Prueba del ejercicio
numeros = [10, 20, 30, 40, 50]
print(promedio_lista(numeros))

# =============================================================================
# 28. Buscar y devolver el primer elemento duplicado en una lista
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada, o None si no hay duplicados.
# =============================================================================

def buscar_duplicado(lista: list) -> any:
    """Encuentra y retorna el primer elemento que se repite en la lista."""
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# Prueba del ejercicio
numeros = [2, 5, 1, 2, 3, 5, 14]
print("Primer duplicado encontrado:", buscar_duplicado(numeros))

# =============================================================================
# 29. Enmascarar caracteres excepto los últimos cuatro
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
# =============================================================================

def enmascarar(texto: any) -> str:
    """Enmascara con '#' todos los caracteres de la representación en string salvo los últimos 4."""
    string = str(texto)
    if len(string) <= 4:
        return string
    return '#' * (len(string) - 4) + string[-4:]

# Pruebas del ejercicio
print(enmascarar("1234567890123456"))
print(enmascarar(987654321))
print(enmascarar("hola"))

# =============================================================================
# 30. Comprobación de anagramas entre dos palabras
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
# =============================================================================

def es_anagrama(palabra1: str, palabra2: str) -> bool:
    """Comprueba si dos palabras contienen exactamente las mismas letras ordenadas."""
    p1 = palabra1.lower().strip()
    p2 = palabra2.lower().strip()
    return sorted(p1) == sorted(p2)

# Pruebas del ejercicio
print("¿Roma y Amor son anagramas?:", es_anagrama("Roma", "Amor"))
print("¿Python y Java son anagramas?:", es_anagrama("Python", "Java"))

# =============================================================================
# 31. Búsqueda de nombre en lista con excepción ValueError
# Crea una función que solicite una lista de nombres y luego un nombre para buscar. Si el nombre está en la lista imprime un mensaje de confirmación; de lo contrario lanza una excepción.
# =============================================================================

def buscar_nombre(nombres_lista: list[str], buscado: str) -> bool:
    """Busca un nombre en una lista o lanza ValueError si no está presente."""
    nombres = [nombre.strip().lower() for nombre in nombres_lista]
    buscado_clean = buscado.strip().lower()
    
    if buscado_clean in nombres:
        print(f"¡El nombre '{buscado}' está en la lista!")
        return True
    else:
        raise ValueError(f"El nombre '{buscado}' no está en la lista.")

# Pruebas del ejercicio
lista_nombres = ["Ana", "Carlos", "Beatriz", "David"]
try:
    buscar_nombre(lista_nombres, "Carlos")
    buscar_nombre(lista_nombres, "Lucas")
except ValueError as e:
    print(f"Excepción capturada: {e}")

# =============================================================================
# 32. Búsqueda del puesto de un empleado en un catálogo
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que no trabaja aquí.
# =============================================================================

def buscar_puesto_empleado(nombre_completo: str, empleados: list[dict]) -> str:
    """Devuelve el puesto laboral de un empleado o mensaje de no coincidencia."""
    nombre_buscado = nombre_completo.strip().lower()
    for empleado in empleados:
        if empleado["nombre"].strip().lower() == nombre_buscado:
            return empleado["puesto"]
    return "La persona no trabaja aquí."

# Prueba del ejercicio
lista_empleados = [
    {"nombre": "Ana", "puesto": "Frontend Engineer"},
    {"nombre": "Carlos", "puesto": "Data Engineer"},
    {"nombre": "Beatriz", "puesto": "Tech Lead"}
]

print("Carlos:", buscar_puesto_empleado("Carlos", lista_empleados))
print("Ana:", buscar_puesto_empleado("ana", lista_empleados))
print("Pedro:", buscar_puesto_empleado("Pedro", lista_empleados))

# =============================================================================
# 33. Suma elemento a elemento de dos listas con lambda
# Crea una función lambda que sume los elementos correspondientes de dos listas dadas con zip.
# =============================================================================

sumar_listas = lambda l1, l2: [x + y for x, y in zip(l1, l2)]

# Prueba del ejercicio
print(sumar_listas([5, 10, 15], [2, 4, 6]))

# =============================================================================
# 34. POO: Clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles:
# - crecer_tronco: aumenta la longitud del tronco en 1 unidad.
# - nueva_rama: añade una nueva rama de longitud 1 a la lista.
# - crecer_ramas: aumenta en 1 unidad la longitud de todas las ramas existentes.
# - quitar_rama(posicion): elimina la rama en la posición indicada.
# - info_arbol: devuelve un string con información de tronco, ramas y longitudes.
# =============================================================================

class Arbol:
    """Clase que representa un árbol con tronco y ramas dinámicas."""

    def __init__(self):
        self.longitud_tronco: int = 1
        self.ramas: list[int] = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.longitud_tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion: int):
        """Elimina la rama situada en una posición específica (índice 0 o 1-based seguro)."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"No existe rama en la posición {posicion}.")

    def info_arbol(self) -> str:
        """Devuelve información completa sobre el estado del tronco y las ramas."""
        return (
            f"Tronco: {self.longitud_tronco} m | "
            f"Ramas ({len(self.ramas)}): {self.ramas}"
        )

# Caso de uso completo especificado
arbol = Arbol()
print("Inicial:", arbol.info_arbol())

arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
print("Antes de podar:", arbol.info_arbol())

arbol.quitar_rama(2)
print("Resultado final:", arbol.info_arbol())

# =============================================================================
# 35. POO: Clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos:
# - agregar_dinero(cantidad)
# - retirar_dinero(cantidad): lanza error si excede saldo o no tiene cuenta
# - transferir_dinero(origen, cantidad): transfiere fondos desde otro usuario con manejo de errores.
# =============================================================================

class SaldoInsuficienteError(Exception):
    pass

class CuentaCorrienteRequeridaError(Exception):
    pass

class UsuarioBanco:
    """Gestiona saldo y transferencias bancarias entre usuarios."""

    def __init__(self, nombre: str, saldo: float, tiene_cuenta_corriente: bool):
        self.nombre = nombre
        self.saldo = float(saldo)
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def agregar_dinero(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")
        self.saldo += cantidad
        print(f"Se agregaron {cantidad}€ a {self.nombre}. Saldo: {self.saldo}€")

    def retirar_dinero(self, cantidad: float):
        if not self.tiene_cuenta_corriente:
            raise CuentaCorrienteRequeridaError(f"{self.nombre} no tiene cuenta corriente para retirar.")
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente ({self.saldo}€) para retirar {cantidad}€.")
        self.saldo -= cantidad
        print(f"{self.nombre} retiró {cantidad}€. Saldo restante: {self.saldo}€")

    def transferir_dinero(self, origen: 'UsuarioBanco', cantidad: float):
        """Transfiere fondos desde el usuario 'origen' hacia este usuario (self)."""
        print(f"Intentando transferir {cantidad}€ de {origen.nombre} a {self.nombre}...")
        origen.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

# Caso de uso del enunciado:
# a. Alicia (100) y Bob (50), ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, tiene_cuenta_corriente=True)
bob = UsuarioBanco("Bob", 50, tiene_cuenta_corriente=True)

# b. Agregar 20 a Bob (saldo pasa a 70).
bob.agregar_dinero(20)

# c. Transferir 80 de Bob a Alicia (debe fallar y capturarse porque Bob tiene 70).
try:
    alicia.transferir_dinero(bob, 80)
except SaldoInsuficienteError as e:
    print(f"Excepción capturada con éxito: {e}")

# d. Retirar 50 del saldo de Alicia (pasa de 100 a 50).
alicia.retirar_dinero(50)

print(f"Saldos finales -> Alicia: {alicia.saldo}€ | Bob: {bob.saldo}€")

# =============================================================================
# 36. Procesamiento de texto modular con subfunciones
# Crea una función llamada procesar_texto que reciba un texto, una opción ('contar', 'reemplazar', 'eliminar') y argumentos variables:
# - contar_palabras: cuenta frecuencia de cada palabra y devuelve dict.
# - reemplazar_palabras: sustituye palabra_original por palabra_nueva.
# - eliminar_palabra: elimina una palabra del texto.
# =============================================================================

def contar_palabras(texto: str) -> dict:
    frecuencias = {}
    for palabra in texto.split():
        limpia = palabra.strip(",.¡!¿?").lower()
        frecuencias[limpia] = frecuencias.get(limpia, 0) + 1
    return frecuencias

def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto: str, palabra: str) -> str:
    palabras = texto.split()
    filtradas = [p for p in palabras if p.strip(",.¡!¿?").lower() != palabra.lower()]
    return " ".join(filtradas)

def procesar_texto(texto: str, opcion: str, *args):
    """Procesa un texto según la opción ('contar', 'reemplazar', 'eliminar')."""
    op = opcion.lower().strip()
    if op == "contar":
        return contar_palabras(texto)
    elif op == "reemplazar":
        if len(args) < 2:
            raise ValueError("Se requieren palabra_original y palabra_nueva para reemplazar.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif op == "eliminar":
        if len(args) < 1:
            raise ValueError("Se requiere la palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción desconocida: '{opcion}'.")

# Pruebas del ejercicio
frase = "Python es genial y Python es potente"
print("Contar:", procesar_texto(frase, "contar"))
print("Reemplazar:", procesar_texto(frase, "reemplazar", "genial", "fantástico"))
print("Eliminar:", procesar_texto(frase, "eliminar", "potente"))

# =============================================================================
# 37. Determinación del momento del día según la hora
# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario (formato 0-23).
# =============================================================================

def determinar_franja_horaria(hora: int) -> str:
    """Devuelve si es de día, tarde o noche según la hora (0-23)."""
    if not (0 <= hora <= 23):
        return "Error: La hora debe estar entre 0 y 23."
    
    if 6 <= hora < 12:
        return f"A las {hora}:00 hrs es de DÍA (Mañana)."
    elif 12 <= hora < 20:
        return f"A las {hora}:00 hrs es de TARDE."
    else:
        return f"A las {hora}:00 hrs es de NOCHE."

# Pruebas del ejercicio
print(determinar_franja_horaria(8))
print(determinar_franja_horaria(16))
print(determinar_franja_horaria(22))

# =============================================================================
# 38. Calificación cualitativa según nota numérica
# Escribe un programa que determine qué calificación en texto tiene un alumno:
# - 0 - 69: insuficiente
# - 70 - 79: bien
# - 80 - 89: muy bien
# - 90 - 100: excelente
# =============================================================================

def obtener_calificacion_texto(nota: float) -> str:
    """Devuelve la calificación cualitativa para una nota entre 0 y 100."""
    if nota < 0 or nota > 100:
        return "Calificación inválida. Debe estar entre 0 y 100."
    
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    else:
        return "excelente"

# Pruebas del ejercicio
for n in [45, 74, 88, 98]:
    print(f"Nota {n}: {obtener_calificacion_texto(n)}")

# =============================================================================
# 39. Cálculo del área de figuras geométricas
# Escribe una función que tome dos parámetros: figura ('rectangulo', 'circulo', 'triangulo') y datos (tupla con medidas):
# - rectangulo: (base, altura) -> base * altura
# - circulo: (radio,) -> pi * radio^2
# - triangulo: (base, altura) -> (base * altura) / 2
# =============================================================================

import math

def calcular_area(figura: str, datos: tuple) -> float:
    """Calcula el área geométrica de la figura especificada."""
    figura_norm = figura.lower().strip()
    
    if figura_norm == "rectangulo":
        base, altura = datos[0], datos[1]
        return base * altura
    elif figura_norm == "circulo":
        radio = datos[0]
        return math.pi * (radio ** 2)
    elif figura_norm == "triangulo":
        base, altura = datos[0], datos[1]
        return (base * altura) / 2
    else:
        raise ValueError(f"Figura '{figura}' no reconocida.")

# Pruebas del ejercicio
print("Área rectángulo (5, 10):", calcular_area("rectangulo", (5, 10)))
print("Área círculo (3,):", round(calcular_area("circulo", (3,)), 2))
print("Área triángulo (6, 4):", calcular_area("triangulo", (6, 4)))

# =============================================================================
# 40. Cálculo de precio final de compra con cupón de descuento
# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea:
# - Solicitar precio original.
# - Preguntar si tiene cupón y su porcentaje (1-100).
# - Aplicar descuento si es válido y mostrar el monto final.
# =============================================================================

def calcular_precio_final(precio_original: float, tiene_cupon: bool = False, cupon_porcentaje: float = 0.0) -> float:
    """Aplica descuento a una compra si el cupón es válido (entre 0 y 100%)."""
    if precio_original <= 0:
        print("El precio debe ser mayor a 0.")
        return 0.0
        
    if tiene_cupon and 0 < cupon_porcentaje <= 100:
        descuento = precio_original * (cupon_porcentaje / 100)
        final = precio_original - descuento
        print(f"Cupón del {cupon_porcentaje}% aplicado (-{descuento:.2f}€). Total: {final:.2f}€")
        return final
    else:
        print(f"Sin descuento aplicable. Total a pagar: {precio_original:.2f}€")
        return precio_original

# Pruebas del ejercicio
print("--- Caso 1: Compra con 20% de descuento ---")
calcular_precio_final(100.0, tiene_cupon=True, cupon_porcentaje=20.0)

print()
print("--- Caso 2: Compra sin cupón ---")
calcular_precio_final(85.5, tiene_cupon=False)
