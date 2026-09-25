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

# 19 Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
# 20 Crea una función que calcule el cubo de un número dado mediante una función lambda.

# 21 Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

# 22 Concatena una lista de palabras. Usa la función reduce().

# 23 Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# 24 Crea una función que cuente el número de caracteres en una cadena de texto dada.

# 25 Crea una función lambda que calcule el resto de la división entre dos números dados.

# 26 Crea una función que calcule el promedio de una lista de números.

# 27 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# 28 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

# 29 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# 30 Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

# 31 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# 32 Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# 33 Crea la clase Arbol

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

# 35 Crea una función llamada procesar_texto

    #     Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
    #     Código a seguir:

    #         Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
    #         Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
    #         Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
    #         Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

    #     Caso de uso:
    #         Verificar el funcionamiento completo de procesar_texto.

# 37 Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# 38 Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.

    #     Reglas:
    #             0 - 69: insuficiente
    #             70 - 79: bien
    #             80 - 89: muy bien
    #             90 - 100: excelente

# 39 Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# 40 Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    #     a. Solicitar al usuario el precio original de un artículo.
    #     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    #     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    #     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    #     e. Mostrar el precio final de la compra, considerando o no el descuento.
    #     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.