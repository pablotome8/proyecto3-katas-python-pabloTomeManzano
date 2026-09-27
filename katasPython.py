# 1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

    # def frecuencia_caracteres(texto):
    #     texto_lower=texto.lower()
    #     dict_letras ={}

    #     for letra in texto_lower:
    #         if letra == " ":
    #             continue
    #         elif letra not in dict_letras:
    #             dict_letras[letra] = 1
    #         else:
    #             dict_letras[letra] +=1
        
    #     return dict_letras
    # cadena_texto = input('Introduce el texto: ')
    # print(frecuencia_caracteres(cadena_texto))

# 2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

    # def doble_valor(lista):
    #     return list(map(lambda x: x*2, lista))

    # lista = [1,2,3,4,5,6,7,8,9]
    # print(doble_valor(lista))

# 3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

    # def buscar_palabra(lista,palabra_objetivo):
    #     resultado =[]
        
    #     for palabra in lista:
    #         if palabra_objetivo.lower() in palabra.lower():
    #             resultado.append(palabra)
                
    #     return resultado
    # palabras = ['leon','camion','conductor','cuidador','explosion','reventon','cuchara','pedro']
    # print(buscar_palabra(palabras,'on'))

# 4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

    # def diferencia_valor(lista1,lista2):
    #     return list(map(lambda x, y: x - y, lista1, lista2))


    # l1 = [10, 20, 30, 40]
    # l2 = [3, 5, 10, 15]

    # resultado = diferencia_valor(l1, l2)
    # print(resultado)

# 4 Importando modulo

    # from operator import sub

    # def diferencia_listas(lista1, lista2):
    #     return list(map(sub, lista1, lista2))

# 5 Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
    
    # def calcular_media(lista_notas,nota_aprobado=5):
        
    #     media = sum(lista_notas) / len(lista_notas)
    #     estado = "aprobado" if media >= nota_aprobado else "suspenso"
        
    #     return (media, estado)
    # notas_alumno1 = [4, 6, 5, 7, 3]
    # media1, estado1 = calcular_media(notas_alumno1)
    # print(f"Media: {media1}, Estado: {estado1}")

# 6 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

        # def dividir_numeros():
        #     try:
        #         num1 = float(input("Introduce el primer número: "))
        #         num2 = float(input("Introduce el segundo número: "))
                
        #         resultado = num1 / num2

        #     except ValueError:
        #         print(" Error: Debes ingresar valores numéricos.")
                
        #     except ZeroDivisionError:
        #         print(" Error: No se puede dividir entre cero.")
                
        #     else:
        #         print(f" Éxito: El resultado de {num1} / {num2} es {resultado}")
        #         print("La división fue exitosa.")

        # dividir_numeros()

# 7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
    
    # def conversor_tupla_string(tupla):
    #     return list(map(lambda t: " ".join(t),tupla))

    # tuplas = [('Hola', 'Mundo'), ('Python', 'es', 'genial'), ('Katas', '2026')]
    # resultado = conversor_tupla_string(tuplas)

    # print(resultado)
   
# 8 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

    # def filtrar_mascotas(lista_mascotas):
    #     prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    #     return list(filter(lambda mascotas: mascotas not in prohibidas, lista_mascotas))
    # mis_mascotas = ["Perro", "Tigre", "Gato", "Mapache", "Hámster", "Oso"]
    # resultado = filtrar_mascotas(mis_mascotas)

    # print(resultado)

# 9 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
    
    # class ListaVaciaError(Exception):
    #     """Excepción para lista de números vacía."""
    #     pass

    # def calculo_promedio(lista_numeros):
    #     if not lista_numeros:
    #         raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
        
    #     return sum(lista_numeros) / len(lista_numeros)

    # try:
    #     resultado = calculo_promedio([10, 20, 30])
    #     # print(f"El promedio es: {resultado}")  # Salida: El promedio es: 20.0
    # except ListaVaciaError as e:
    #     # print(f"Error capturado: {e}")

# 10 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
   
    # class EdadFueraDeRango(Exception):
    #     """Excepcion para edad fuera de rango"""
    #     pass

    #  def solicitar_edad():
    #     try:
    #         entrada = input("Por favor, introduce tu edad: ")
    #         edad = int(entrada)
            
    #         if edad < 0 or edad > 120:
    #             raise EdadFueraDeRango(f"La edad {edad} está fuera del rango permitido (0-120).")

    #     except ValueError as e:
    #         print(f"Debes ingresar un número entero válido.")
    #         print(f"Detalle interno: {e}")

    #     except EdadFueraDeRango as e:
    #         print(f" Error de validación: {e}")

    #     else:
    #         print(f"Edad registrada c({edad} años).")


    # solicitar_edad()

# 11 Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
    
    # def longitud_palabras(frase):
    #     palabras = frase.split()
        
    #     return list(map(len, palabras))

    # texto = "Me esta costando de cojones aprender Python"
    # resultado = longitud_palabras(texto)

    # print(resultado)

# 12 Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

    # def map_mayus_minus(caracteres):
    #     unicos = set(caracteres)
        
    #     return list(map(lambda c: (c.upper(), c.lower()), unicos))

    # letras = ["a", "b", "c", "a", "B", "C", "d"]
    # resultado = map_mayus_minus(letras)

    # print(resultado)

# 13 Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

    # def palabras_por_letra(lista, letra_inicio):
    #     return list(filter(lambda palabra: palabra.lower().startswith(letra_inicio.lower()), lista))

    # palabras = ["perro", "gato", "pájaro", "pez", "hamster"]
    # print(palabras_por_letra(palabras, "p"))
    
# 14 Crea una función lambda que sume 3 a cada número de una lista dada.

    # def sumar_tres(lista_numeros):
    #     return list(map(lambda x: x + 3, lista_numeros))

    # numeros = [1, 5, 10, 15, 20]
    # resultado = sumar_tres(numeros)

    # print(resultado)
    
# 15 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
    
    # def filtrar_palabras_largas(texto, n):
    #     palabras = texto.split()
        
    #     return list(filter(lambda palabra: len(palabra) > n, palabras))

    # frase = "Aprender a programar en Python es un fumon"
    # longitud_minima = 5

    # resultado = filtrar_palabras_largas(frase, longitud_minima)

    # print(resultado)

# 16 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

    # from functools import reduce

    # def digitos_a_numero(lista_digitos):
        
    #     return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)

    # digitos = [5, 7, 2]
    # resultado = digitos_a_numero(digitos)

    # print(resultado)

# 17 Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

    # estudiantes = [
    #     {"nombre": "Papote", "edad": 20, "calificación": 9},
    #     {"nombre": "Robertototo", "edad": 22, "calificación": 5},
    #     {"nombre": "RosaMelano", "edad": 21, "calificación": 9},
    #     {"nombre": "BenitoCamela", "edad": 19, "calificación": 6},
    #     {"nombre": "ElverGalarga", "edad": 23, "calificación": 3}
    # ]

    # estudiantes_sobresalientes = list(
    #     filter(lambda est: est["calificación"] >= 9, estudiantes)
    # )

    # print(estudiantes_sobresalientes)

# 18 Crea una función lambda que filtre los números impares de una lista dada.

    # def filtro_impares(lista_numeros):
    #     return list(map(lambda x: x % 2 !=0,lista_numeros))

    # numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # impares = filtro_impares(numeros)

    # print(impares)

# 19 Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

    # def buscar_enteros(lista_mixta):
    #     return list(filter(lambda x: isinstance(x,int), lista_mixta))

    # lista_elementos = [10, "hola", 25, "python", 100, "katas", True]
    # enteros = buscar_enteros(lista_elementos)

    # print(enteros)
                
                
# 20 Crea una función que calcule el cubo de un número dado mediante una función lambda.

    # def calculo_cubo(numero):
    #     cubo = lambda x: x**3
    #     return cubo(numero)

    # valor = 3
    # resultado_cubo = calculo_cubo(valor)

    # print(resultado_cubo)


# 21 Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

    # from functools import reduce

    # def total_valores(lista_numeros):
    #     return reduce(lambda acumulado,x: acumulado*x,lista_numeros)

    # numeros = [1,2,3,4,5,6,7,8,9]
    # resultado_final= total_valores(numeros)

    # print(resultado_final)
    
# 22 Concatena una lista de palabras. Usa la función reduce().

    # from functools import reduce

    # def concatenar_palabras(lista_palabras):
    #     return reduce(lambda p,p2: p+" "+p2,lista_palabras)

    # palabras = ["Hola", "mundo", "desde", "Python"]
    # resultado = concatenar_palabras(palabras)

    # print(resultado)


# 23 Calcula la diferencia total en los valores de una lista. Usa la función reduce().
    
    # from functools import reduce

    # def diferencia_valores(lista_valores):
    #     return reduce(lambda x,x1: x-x1,lista_valores)

    # numeros = [100, 20, 10, 5]
    # resultado = diferencia_valores(numeros)

    # print(resultado)

# 24 Crea una función que cuente el número de caracteres en una cadena de texto dada.

    # from functools import reduce

    # def calculo_caracteres_totales(lista_palabras):
    #     return sum(map(len,lista_palabras))

    # palabras = ["hola", "cola", "pa", "ti"]
    # resultado = calculo_caracteres_totales(palabras)

    # print(resultado)

# 25 Crea una función lambda que calcule el resto de la división entre dos números dados.

    # def resto_division(numero1,numero2):
    #     resto= lambda a,b: a%b
    #     return resto (numero1,numero2)

    # print(resto_division(10,3))

# 26 Crea una función que calcule el promedio de una lista de números.

    # def calcular_promedio(lista_numeros):
    #     return sum(lista_numeros)/len(lista_numeros)
    # numeros = [10, 20, 30, 40, 50]
    # resultado = calcular_promedio(numeros)

    # print(resultado)

# 27 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
 
    # def buscar_duplicado(lista):
    #     no_duplicados = set()
    #     for elemento in lista:
    #         if elemento in no_duplicados:
    #             return elemento  #Aqui devolverias el primer elemento al encontrar coincidencia en el set
    #         else:
    #             no_duplicados.add(elemento)
    #     return None

    # numeros = [2, 5, 1, 2, 3, 5, 14]
    # resultado = buscar_duplicado(numeros)

    # print(resultado)

# 28 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

    # def enmascarar(texto):
    #     string = str(texto)
        
    #     if len(string) <= 4:
    #         return string
        
    #     return '#' * (len(string) - 4) + string[-4:]

    # # 29 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

    # def es_anagrama(palabra1: str, palabra2: str) -> bool:
    #     # Convierto a minusculas
    #     p1 = palabra1.lower()
    #     p2 = palabra2.lower()
        
    #     return sorted(p1) == sorted(p2)

# 30 Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

    # def buscar_nombre():
    #     entrada = input("Ingresa una lista de nombres (separados por comas): ")
        
    #     nombres = [nombre.strip() for nombre in entrada.split(",") if nombre.strip()]
        
    #     buscado = input("Ingresa el nombre que deseas buscar: ").strip()
        
    #     if buscado in nombres:
    #         print(f"¡El nombre '{buscado}' fue encontrado en la lista!")
    #     else:
    #         # Lanzamos una excepción personalizada si no existe
    #         raise ValueError(f"El nombre '{buscado}' no se encuentra en la lista.")

    # try:
    #     buscar_nombre()
    # except ValueError as e:
    #     print(f"Excepción capturada: {e}")

# 31 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

    # def buscar_puesto_empleado(nombre_completo: str, empleados: list) -> str:
    #     nombre_buscado = nombre_completo.strip().lower()
        
    #     for empleado in empleados:
    #         if empleado["nombre"].strip().lower() == nombre_buscado:
    #             return empleado["puesto"]
                
    #     return "La persona no trabaja aquí."


    # lista_empleados = [
    #     {"nombre": "Ana", "puesto": " Frontend"},
    #     {"nombre": "Carlos", "puesto": "Data"},
    #     {"nombre": "Beatriz", "puesto": "Gerente"}
    # ]

    # print(buscar_puesto_empleado("Carlos", lista_empleados)) 

    # print(buscar_puesto_empleado("ana", lista_empleados)) 

    # print(buscar_puesto_empleado("Pedro", lista_empleados)) 

# 32 Crea una función lambda que sume elementos correspondientes de dos listas dadas.

    # sumar_listas = lambda l1, l2: [x + y for x, y in zip(l1, l2)]

    # print(sumar_listas([5, 10, 15], [2, 4, 6])) 
    
# 33 Crea la clase Arbol #Me he acordado ahora de la extension esa de auatoDocstring

    #         Define un árbol genérico con un tronco y ramas como atributos.
    #         Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
    #         Código a seguir:

    #             Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    #             Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    #             Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    #             Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    #             Implementar el método quitar_rama para eliminar una rama en una posición específica.
    #             Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

    #         Caso de uso:
    #                 a. Crear un árbol.
    #                 b. Hacer crecer el tronco una unidad.
    #                 c. Añadir una nueva rama.
    #                 d. Hacer crecer todas las ramas una unidad.
    #                 e. Añadir dos nuevas ramas.
    #                 f. Retirar la rama situada en la posición 2.
    #                 g. Obtener información sobre el árbol.

        # class Arbol:
        #     def __init__(self):
        #         self.tronco = 1
        #         self.ramas = []

        #     def crecer_tronco(self):
        #         """Aumenta la longitud del tronco en una unidad."""
        #         self.tronco += 1

        #     def nueva_rama(self):
        #         """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        #         self.ramas.append(1)

        #     def crecer_ramas(self):
        #         """Aumenta en una unidad la longitud de todas las ramas existentes."""
        #         self.ramas = [rama + 1 for rama in self.ramas]

        #     def quitar_rama(self, posicion: int):
        #         """Elimina una rama en una posición específica (índice 0-based)."""
        #         if 0 <= posicion < len(self.ramas):
        #             self.ramas.pop(posicion)
        #         else:
        #             print(f"Error: La posición {posicion} no existe en la lista de ramas.")

        #     def info_arbol(self) -> str:
        #         """Devuelve información sobre el tronco, el número de ramas y sus longitudes."""
        #         return (
        #             f"Información del árbol:\n"
        #             f" - Longitud del tronco: {self.tronco}\n"
        #             f" - Número de ramas: {len(self.ramas)}\n"
        #             f" - Longitudes de las ramas: {self.ramas}"
        #         )

        # mi_arbol = Arbol()

        # mi_arbol.crecer_tronco()

        # mi_arbol.nueva_rama()

        # mi_arbol.crecer_ramas()

        # mi_arbol.nueva_rama()
        # mi_arbol.nueva_rama()

        # mi_arbol.quitar_rama(2)

        # print(mi_arbol.info_arbol())

# 34 Crea la clase UsuarioBanco

    #     Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
    #     Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
    #     Código a seguir:

    #         Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
    #         Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
    #         Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
    #         Implementar agregar_dinero para aumentar el saldo del usuario.

    #     Caso de uso:
    #             a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    #             b. Agregar 20 unidades al saldo de Bob.
    #             c. Transferir 80 unidades de Bob a Alicia.
    #             d. Retirar 50 unidades del saldo de Alicia.
    
        # class UsuarioBanco:
        #     def __init__(self, nombre: str, saldo: float, tiene_cuenta_corriente: bool):
        #         """Inicializa un usuario con su nombre, saldo e indicador de cuenta corriente."""
        #         self.nombre = nombre
        #         self.saldo = float(saldo)
        #         self.tiene_cuenta_corriente = tiene_cuenta_corriente

        #     def agregar_dinero(self, cantidad: float):
        #         """Aumenta el saldo del usuario."""
        #         if cantidad <= 0:
        #             raise ValueError("La cantidad a agregar debe ser mayor que 0.")
        #         self.saldo += cantidad
        #         print(f"[{self.nombre}] Se han agregado {cantidad}€. Nuevo saldo: {self.saldo}€")

        #     def retirar_dinero(self, cantidad: float):
        #         """Sustrae dinero del saldo, lanzando un error si la cantidad excede el saldo actual."""
        #         if cantidad <= 0:
        #             raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        #         if cantidad > self.saldo:
        #             raise ValueError(
        #                 f"[{self.nombre}] Saldo insuficiente. Intenta retirar {cantidad}€ pero solo tiene {self.saldo}€."
        #             )
        #         self.saldo -= cantidad
        #         print(f"[{self.nombre}] Se han retirado {cantidad}€. Nuevo saldo: {self.saldo}€")

        #     def transferir_dinero(self, origen: 'UsuarioBanco', cantidad: float):
        #         """
        #         Transfiere dinero DESDE otro usuario (origen) HACIA este usuario (self).
        #         Lanza un error si el usuario de origen no puede realizar la retirada.
        #         """
        #         print(f"Iniciando transferencia de {cantidad}€ desde {origen.nombre} hacia {self.nombre}...")
                
        #         origen.retirar_dinero(cantidad)
                
        #         self.saldo += cantidad
        #         print(f"[{self.nombre}] Transferencia recibida. Nuevo saldo: {self.saldo}€")



        # alicia = UsuarioBanco("Alicia", 100, tiene_cuenta_corriente=True)
        # bob = UsuarioBanco("Bob", 50, tiene_cuenta_corriente=True)

        # print(f"Estado inicial -> Alicia: {alicia.saldo}€ | Bob: {bob.saldo}€\n")

        # print("--- Paso b: Agregar 20 unidades a Bob ---")
        # bob.agregar_dinero(20)

        # print(f"\nEstado actual -> Alicia: {alicia.saldo}€ | Bob: {bob.saldo}€\n")

        # print("--- Paso c: Transferir 80 unidades de Bob a Alicia ---")
        # try:
        #     alicia.transferir_dinero(bob, 80)
        # except ValueError as e:
        #     print(f"Error en la transferencia: {e}")

        # print(f"\nEstado actual -> Alicia: {alicia.saldo}€ | Bob: {bob.saldo}€\n")

        # print("--- Paso d: Retirar 50 unidades de Alicia ---")
        # try:
        #     alicia.retirar_dinero(50)
        # except ValueError as e:
        #     print(f"Error al retirar dinero: {e}")

        # print(f"\nEstado final -> Alicia: {alicia.saldo}€ | Bob: {bob.saldo}€")

# 35 Crea una función llamada procesar_texto

    #     Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
    #     Código a seguir:

    #         Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
    #         Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
    #         Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
    #         Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

    #     Caso de uso:
    #         Verificar el funcionamiento completo de procesar_texto.
    
        # import re
        # from collections import Counter


        # def contar_palabras(texto: str) -> dict:
        #     """Cuenta el número de veces que aparece cada palabra en el texto."""
        #     palabras = re.findall(r'\b\w+\b', texto.lower())
        #     return dict(Counter(palabras))


        # def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
        #     """Sustituye una palabra_original por una palabra_nueva en el texto."""
        #     patron = rf'\b{re.escape(palabra_original)}\b'
        #     return re.sub(patron, palabra_nueva, texto, flags=re.IGNORECASE)


        # def eliminar_palabra(texto: str, palabra: str) -> str:
        #     """Elimina todas las ocurrencias de una palabra en el texto."""
        #     patron = rf'\b{re.escape(palabra)}\b'
        #     texto_limpio = re.sub(patron, '', texto, flags=re.IGNORECASE)
        #     return re.sub(r'\s+', ' ', texto_limpio).strip()


        # def procesar_texto(texto: str, opcion: str, *args):
        #     """
        #     Procesa un texto según la opción especificada:
        #     - 'contar': sin argumentos adicionales.
        #     - 'reemplazar': requiere (palabra_original, palabra_nueva).
        #     - 'eliminar': requiere (palabra_a_eliminar).
        #     """
        #     opcion = opcion.lower().strip()

        #     if opcion == "contar":
        #         return contar_palabras(texto)

        #     elif opcion == "reemplazar":
        #         if len(args) < 2:
        #             raise ValueError("La opción 'reemplazar' requiere dos argumentos: palabra_original y palabra_nueva.")
        #         return reemplazar_palabras(texto, args[0], args[1])

        #     elif opcion == "eliminar":
        #         if len(args) < 1:
        #             raise ValueError("La opción 'eliminar' requiere un argumento: palabra_a_eliminar.")
        #         return eliminar_palabra(texto, args[0])

        #     else:
        #         raise ValueError(f"Opción no válida: '{opcion}'. Opciones permitidas: 'contar', 'reemplazar', 'eliminar'.")



        # texto_ejemplo = "El perro corre en el parque. El perro es muy rápido."

        # print("Texto original:")
        # print(f'"{texto_ejemplo}"\n')

        
        # resultado_contar = procesar_texto(texto_ejemplo, "contar")
        # print("--- 1. Contar palabras ---")
        # print(resultado_contar)
        # print()

        
        # resultado_reemplazar = procesar_texto(texto_ejemplo, "reemplazar", "perro", "gato")
        # print("--- 2. Reemplazar 'perro' por 'gato' ---")
        # print(f'"{resultado_reemplazar}"')
        # print()

        
        # resultado_eliminar = procesar_texto(texto_ejemplo, "eliminar", "rápido")
        # print("--- 3. Eliminar la palabra 'rápido' ---")
        # print(f'"{resultado_eliminar}"')

# 37 Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

    # def determinar_franja_horaria():
    #     try:
    #         hora_input = input("Ingresa la hora en formato de 24 horas (0-23): ")
    #         hora = int(hora_input)

    #         if hora < 0 or hora > 23:
    #             print("Error: La hora debe ser un número entero entre 0 y 23.")
    #             return

    #         if 6 <= hora < 12:
    #             print(f"A las {hora}:00 hrs es de DÍA (Mañana).")
    #         elif 12 <= hora < 20:
    #             print(f"A las {hora}:00 hrs es de TARDE.")
    #         else:
    #             print(f"A las {hora}:00 hrs es de NOCHE.")

    #     except ValueError:
    #         print("Error: Por favor, ingresa un número entero válido.")

    # determinar_franja_horaria()
    
# 38 Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.

    #     Reglas:
    #             0 - 69: insuficiente
    #             70 - 79: bien
    #             80 - 89: muy bien
    #             90 - 100: excelente
    
        # def obtener_calificacion_texto(nota: float) -> str:
        #     """Devuelve la calificación en texto correspondiente a una nota numérica."""
        #     if nota < 0 or nota > 100:
        #         return "Calificación inválida. Debe estar entre 0 y 100."

        #     if 0 <= nota <= 69:
        #         return "insuficiente"
        #     elif 70 <= nota <= 79:
        #         return "bien"
        #     elif 80 <= nota <= 89:
        #         return "muy bien"
        #     else:  # 90 <= nota <= 100
        #         return "excelente"


        # def solicitar_calificacion():
        #     try:
        #         entrada = input("Ingresa la calificación del alumno (0-100): ")
        #         nota = float(entrada)

        #         resultado = obtener_calificacion_texto(nota)
        #         print(f"Resultado: {resultado}")

        #     except ValueError:
        #         print("Error: Por favor, ingresa un número válido.")


        # solicitar_calificacion()

# 39 Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

    # import math

    # def calcular_area(figura: str, datos: tuple) -> float:
    #     """
    #     Calcula el área de la figura geométrica especificada.
        
    #     Parámetros:
    #     - figura: "rectangulo", "circulo" o "triangulo"
    #     - datos: tupla con las medidas necesarias:
    #         - "rectangulo": (base, altura)
    #         - "circulo": (radio,)
    #         - "triangulo": (base, altura)
    #     """
    #     figura_norm = figura.lower().strip()

    #     if figura_norm == "rectangulo":
    #         if len(datos) < 2:
    #             raise ValueError("Para un rectángulo se necesitan base y altura: (base, altura).")
    #         base, altura = datos[0], datos[1]
    #         return base * altura

    #     elif figura_norm == "circulo":
    #         if len(datos) < 1:
    #             raise ValueError("Para un círculo se necesita el radio: (radio,).")
    #         radio = datos[0]
    #         return math.pi * (radio ** 2)

    #     elif figura_norm == "triangulo":
    #         if len(datos) < 2:
    #             raise ValueError("Para un triángulo se necesitan base y altura: (base, altura).")
    #         base, altura = datos[0], datos[1]
    #         return (base * altura) / 2

    #     else:
    #         raise ValueError(
    #             f"Figura no reconocida: '{figura}'. Usar 'rectangulo', 'circulo' o 'triangulo'."
    #         )

    # area_rect = calcular_area("rectangulo", (5, 10))
    # print(f"Área del rectángulo: {area_rect}")  

    # area_circ = calcular_area("circulo", (3,))
    # print(f"Área del círculo: {round(area_circ, 2)}")  

    # area_tri = calcular_area("triangulo", (6, 4))
    # print(f"Área del triángulo: {area_tri}")  

# 40 Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    #     a. Solicitar al usuario el precio original de un artículo.
    #     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    #     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    #     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    #     e. Mostrar el precio final de la compra, considerando o no el descuento.
    #     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
    
        # def calcular_precio_final():
        #     try:
        #         precio_original = float(input("Ingresa el precio original del artículo (€): "))
                
        #         if precio_original <= 0:
        #             print("El precio original debe ser un valor mayor a cero.")
        #             return

        #         tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        #         if tiene_cupon in ["sí", "si", "s"]:
        #             cupon = float(input("Ingresa el valor o porcentaje del cupón de descuento (%): "))

        #             if cupon > 0 and cupon <= 100:
        #                 descuento = precio_original * (cupon / 100)
        #                 precio_final = precio_original - descuento
        #                 print(f"\n¡Cupón del {cupon}% aplicado con éxito!")
        #                 print(f"Descuento aplicado: -{descuento:.2f}€")
        #             elif cupon > 100:
        #                 print("\nEl descuento no puede ser mayor al 100%. Se cobrará el precio original.")
        #                 precio_final = precio_original
        #             else:
        #                 print("\nEl cupón no es válido (debe ser mayor a 0). No se aplicará descuento.")
        #                 precio_final = precio_original

        #         elif tiene_cupon in ["no", "n"]:
        #             print("\nNo se ha aplicado ningún descuento.")
        #             precio_final = precio_original

        #         else:
        #             print("\nRespuesta no reconocida. Se procederá sin aplicar descuento.")
        #             precio_final = precio_original

        #         print(f"Precio final a pagar: {precio_final:.2f}€")

        #     except ValueError:
        #         print("Error: Por favor, ingresa un número válido para los montos.")


        # calcular_precio_final()