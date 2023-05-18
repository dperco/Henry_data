##############################################################################################
########################  INTRO  ###################################

# a=10
# b=20

# print(a*b)

# a=3
# b="a"

# print(a+b)


# a=False
# b=True

# print(type(a))


# a='2'

# print(int(a))

##########################################################################################
######################## VARIABLES TIPO DE DATOS #####################


#1-Crear una variable que contenga un elemento del conjunto de números enteros y luego 
#imprimir por pantalla

# a=(1,2,3,4,5,7,8,9,10)

# print(a) 

# print(type(8.5))

# print(type(a))

# x=True
# z='True'

# print(type(x))
# print (type(z))

# #print (x = z)


# # Definición de los números complejos
# num1 = 3 + 2j
# num2 = 1 - 4j

# # Suma de los números complejos
# resultado = num1 + num2

# # Imprimir el resultado
# print("El resultado de la suma es:", resultado)


# num=2

# result= num **8

# print(result)

# result = 27/4

# entera = 27 // 4

# resto = 27 % 4
# print (result)
# print(entera)
# print(resto)





##################### clase 3 ##############################################
###########################FLUJO DE CONTROL ###############################

# b=-6

# if(b >= 0 ):
#     print("bes mayor a 0")
# else: print("b es menor que cero")

# a=6
# b='6'

# if(type(a) == type(b)):print("a y b son del mismo tipo")
# else:print("NO SON DEL MISMO TIPO")
    

# for i in range(6):
#     resultado = i ** 3
#     print(f"El resultado de elevar {i} a la potencia de 3 es: {resultado}")


# Variable con el número a factorizar
# numero = 24

# # Verificar si el número es un entero mayor a 0
# if isinstance(numero, int) and numero > 0:
#     # Inicializar el contador y el resultado
#     contador = 2
#     resultado = []

#     # Realizar el factoreo
#     while contador <= numero:
#         if numero % contador == 0:
#             resultado.append(contador)
#             numero = numero // contador
#         else:
#             contador += 1

#     # Mostrar el resultado del factoreo
#     print(f"El factoreo de {numero} es: {resultado}")
# else:
#     print("El número no es un entero mayor a 0.")


#Imprimir los números primos existentes entre 0 y 30

# Función para verificar si un número es primo
# def es_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# # Imprimir los números primos entre 0 y 30
# for num in range(2, 31):
#     if es_primo(num):
#         print(num)


#Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, 
#dentro del rango de números de 100 a 300

# Definir límites del rango
# inicio = 100
# fin = 300

# # Inicializar contador
# contador = inicio

# # Ciclo while para imprimir valores divisibles por 12
# while contador <= fin:
#     if contador % 12 != 0:
#         contador += 1
#         continue
#     print(contador)
#     contador += 1

#########Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número 
         #divisible
          # por 3 y además múltiplo de 6
# Definir límites del rango
# inicio = 100
# fin = 300

# # Inicializar contador
# contador = inicio

# # Ciclo while para encontrar el primer número divisible por 3 y múltiplo de 6
# while contador <= fin:
#     if contador % 3 != 0 or contador % 6 != 0:
#         contador += 1
#         continue
#     print("El primer número divisible por 3 y múltiplo de 6 es:", contador)
#     break

################################################################################################
#### ESTRUCTURA DE DATOS ########################################################################

#Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 
#elementos e imprimir por pantalla

# Crear lista de ciudades
# ciudades = ["Nueva York", "Londres", "París", "Tokio", "Roma", "Sídney", "Barcelona", "Estambul"]

# # Filtrar ciudades con más de 5 caracteres
# ciudades_mas_de_5 = [ciudad for ciudad in ciudades if len(ciudad) > 5]

# # Imprimir ciudades por pantalla
# for ciudad in ciudades_mas_de_5:
#     print(ciudad)


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#Visualizar el tipo de dato de la lista


# # Lista de elementos
# lista = [10, "Hola", True, 3.14]

# # Visualizar el tipo de datos de cada elemento
# for elemento in lista:
#     print(f"El tipo de dato de {elemento} es: {type(elemento)}")


# Lista de ciudades existente
# ciudades = ["Nueva York", "Londres", "París"]

# # Agregar una ciudad más a la lista
# ciudades.append("Tokio")

# # Agregar una ciudad que no exista a la lista
# ciudades.append("Berlín")

# # Imprimir la lista actualizada
# print(ciudades)
# Crear una lista de 10 elementos
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Imprimir la lista
# print(lista)

# #Visualizar el tipo de dato de la lista


# print("El tipo de dato de la lista es:", type(lista))

# #Visualizar los primeros 4 elementos de la lista

# print('los primeros 4 elementos', lista[:4])


# #Agregar una ciudad más a la lista 

# lista.append(11)
# print(lista)
# lista.append(4)
# print(lista)


# #Agregar otra ciudad, pero en la cuarta posición

# lista.insert(4,12)
# print(lista)


# #Concatenar otra lista a la ya creada

# lista2=[100,200,300]

# lista_tot=lista+lista2

# print(lista_tot)


# #Encontrar el índice del elem  agregamos duplicada

# print(lista_tot.index(4))

# #print(lista_tot.index(50))


# #Extraer el ultimo elemento de la lista, guardarlo en una variable e imprimirlo

# ultimo_elemento = lista_tot[-1]

# # Imprimir el último elemento
# print("El último elemento de la lista es:", ultimo_elemento)



# #Mostrar la lista multiplicada por 4

# # Multiplicar la lista por 4
# lista_multiplicada = lista_tot * 4

# # Imprimir la lista multiplicada
# print("La lista multiplicada por 4 es:", lista_multiplicada)

# #Crear una tupla que contenga los numeros enteros del 1 al 20

# # Crear una tupla con los números enteros del 1 al 20
# tupla = tuple(range(1, 21))

# # Imprimir la tupla
# print(tupla)


# #Imprimir desde el índice 10 al 15 de la tupla

# elementos = tupla[10:16]
# print(elementos)


# #Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe,
# #  agregarlo. Usando una variable e informar lo sucedido.


# # Validar la existencia del elemento 55
# if 55 in lista_tot:
#     resultado = "El elemento 55 ya existe en la lista."
# else:
#     lista_tot.append(55)
#     resultado = "El elemento 55 fue agregado a la lista."

# # Imprimir el resultado
# print(resultado)
# print(lista_tot)


# #Convertir la tupla en una lista


# # Convertir la tupla en una lista
# lista_conv = list(tupla)

# # Imprimir la lista resultante
# print(tupla)
# print(lista_conv)


# #Crear un diccionario utilizando la lista cradada, asignandole
# #  la clave "par". Agregar tambien otras claves, como puede ser "impar".

# # Crear un diccionario con la clave "par"
# diccionario = dict(zip(lista, ["par" if num % 2 == 0 else "impar" for num in lista]))

# # Imprimir el diccionario
# print(diccionario)

# #Imprimir las claves del diccionario

# # Imprimir las claves del diccionario
# claves = diccionario.keys()
# print(claves)

# claves_lista = list(claves)
# print(claves_lista)

# #Imprimir las ciudades a través de su clave

# # Imprimir los elementos a través de las claves
# for clave in diccionario:
#     print("Clave:", clave)
#     print("Valor:", diccionario[clave])
#     print()

###############################################################################################
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ITERACIONES  ########################################

#A partir de una lista vacía, utilizar un ciclo while para cargar allí 
#números negativos del -15 al -1

# Crear una lista vacía
# lista = []

# # Cargar números negativos del -15 al -1 en la lista
# numero = -15
# while numero <= -1:
#     lista.append(numero)
#     numero += 1

# # Imprimir la lista resultante
# print(lista)

#Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares


# Lista con los números negativos del -15 al -1
# lista = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# # Índice para recorrer la lista
# indice = 0

# # Recorrer la lista e imprimir solo los números pares
# while indice < len(lista):
#     numero = lista[indice]
#     if numero % 2 == 0:
#         print(numero)
#     indice += 1

# #Utilizar la función enumerate para obtener dentro del iterable, tambien el índice al 
# # que corresponde el elemento

# # Recorrer la lista e imprimir solo los números pares junto con su índice
# for indice, numero in enumerate(lista):
#     if numero % 2 == 0:
#         print("Índice:", indice, "- Número par:", numero)

# #Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se 
# # completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# # Lista con los números existentes
# lista_nueva = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]

# # Crear una nueva lista para almacenar los valores completos
# lista_completa = []

# # Iterar desde 1 hasta 20
# for numero in range(1, 21):
#     if numero in lista_nueva:
#         lista_completa.append(numero)
#     else:
#         lista_completa.append(numero)

# # Imprimir la lista completa
# print(lista_completa)


#Crear una lista con los primeros treinta números de la sucesión de fibonacci

# Crear una lista vacía para almacenar los números de Fibonacci
# fibonacci = []

# # Generar los primeros treinta números de Fibonacci
# a, b = 0, 1
# for _ in range(30):
#     fibonacci.append(a)
#     a, b = b, a + b

# # Imprimir la lista de Fibonacci
# print(fibonacci)


#Realizar la suma de todos los elementos de la lista del punto anterior

# def fibonacci_sum(n):
#     fib_list = [0, 1]  # Inicializar la lista con los primeros dos elementos de Fibonacci
#     while len(fib_list) < n:  # Generar la lista de Fibonacci hasta el número deseado
#         fib_list.append(fib_list[-1] + fib_list[-2])

#     # Calcular la suma de los elementos de la lista
#     sum_of_fibonacci = sum(fib_list)
#     return sum_of_fibonacci

# # Ejemplo de uso
# n = 10  # Número de elementos de Fibonacci para generar
# result = fibonacci_sum(n)
# print(f"La suma de los primeros {n} elementos de la serie de Fibonacci es: {result}")

#Con la lista del ejercicio anterior, imprima el cociente de los últimos 5 pares de dos números contiguos:
# Donde i es la cantidad total de elementos
# n i-1 / n i
# n i-2 / n i-1
# n i-3 / n i-2
# n i-4 / n i-3
# n i-5 / n i-4

# def fibonacci_cocientes(n):
#     fib_list = [0, 1]  # Inicializar la lista con los primeros dos elementos de Fibonacci
#     while len(fib_list) < n:  # Generar la lista de Fibonacci hasta el número deseado
#         fib_list.append(fib_list[-1] + fib_list[-2])

#     # Calcular los cocientes de los últimos 5 pares de dos números contiguos
#     cocientes = []
#     for i in range(1, 6):
#         quotient = fib_list[-i-1] / fib_list[-i]
#         cocientes.append(quotient)

#     # Imprimir los cocientes
#     for quotient in cocientes:
#         print(quotient)

# # Ejemplo de uso
# n = 15  # Número de elementos de Fibonacci para generar
# fibonacci_cocientes(n)
# #A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
# #cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'

# cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'

# # Buscar la letra 'n' en la cadena y mostrar las posiciones
# posiciones = []
# for i in range(len(cadena)):
#     if cadena[i] == 'n':
#         posiciones.append(i)

# # Mostrar las posiciones en las que aparece la letra 'n'
# print(f"La letra 'n' aparece en las siguientes posiciones: {posiciones}")

# #Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador

# #cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'

# # Convertir la cadena en una lista de palabras
# lista_cadena = cadena.split()

# # Recorrer la lista con un iterador
# iterador = iter(lista_cadena)

# # Iterar sobre los elementos de la lista con el iterador
# for palabra in iterador:
#     print(palabra)

# #A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7
# #lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]

# # Crear una nueva lista con los números divisibles por 7
# nueva_lista = [num for num in lis if num % 7 == 0]

# # Imprimir la nueva lista
# print(nueva_lista)



# #A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:
# #lis = [[1,2,3,4],'rojo',' verde',[Verdadero,Falso,Falso],['uno','dos','tres']]

# lis = [[1, 2, 3, 4], 'rojo', 'verde', [True, False, False], ['uno', 'dos', 'tres']]

# # Función para contar la cantidad total de elementos en una lista
# def contar_elementos(lista):
#     count = 0
#     for elemento in lista:
#         if isinstance(elemento, list):  # Verificar si el elemento es una lista
#             count += contar_elementos(elemento)  # Llamar recursivamente a la función si es una lista
#         else:
#             count += 1  # Contar el elemento si no es una lista
#     return count

# # Contar la cantidad total de elementos en la lista 'lis'
# cantidad_elementos = contar_elementos(lis)
# print(f"La lista 'lis' contiene {cantidad_elementos} elementos en total.")


# for i in range(len(lis)):
#     if not isinstance(lis[i], list):
#         lis[i] = [lis[i]]

# # Imprimir la lista modificada
# print(lis)


############################################################################################
##################### FUNCIONES ######################################################



#Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# def es_primo(numero):
#     if numero < 2:  # Los números menores a 2 no son primos
#         return False
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# # Ejemplo de uso
# numero = 17
# resultado = es_primo(numero)
# print(resultado)

# #Usando la función del punto 1, realizando otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# def es_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# def obtener_primos(lista_numeros):
#     primos = []
#     for numero in lista_numeros:
#         if es_primo(numero):
#             primos.append(numero)
#     return primos

# # # Ejemplo de uso
# # numeros = [10, 13, 15, 17, 20, 23, 25]
# # primos = obtener_primos(numeros)
# # print(primos)

# #MODAL 
# def valor_modal(self, lista, menor):
#         lista_unicos = []
#         lista_repeticiones = []
#         if len(lista) == 0:
#             return None
#         if (menor):
#             lista.sort()
#         else:
#             lista.sort(reverse=True)
#         for elemento in lista:
#             if elemento in lista_unicos:
#                 i = lista_unicos.index(elemento)
#                 lista_repeticiones[i] += 1
#             else:
#                 lista_unicos.append(elemento)
#                 lista_repeticiones.append(1)
#         moda = lista_unicos[0]
#         maximo = lista_repeticiones[0]
#         for i, elemento in enumerate(lista_unicos):
#             if lista_repeticiones[i] > maximo:
#                 moda = lista_unicos[i]
#                 maximo = lista_repeticiones[i]
#         return moda, maximo

# # #Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# # #Fórmula 1 : (°C × 9/5) + 32 = °F
# # #Fórmula 2 : °C + 273.15 = °K
# # #Debe recibir 3 parámetros: el valor, la medida de origen y la medida de destino


# def convertir_temperatura(valor, medida_origen, medida_destino):
#     if medida_origen == "C" and medida_destino == "F":
#         resultado = (valor * 9/5) + 32
#     elif medida_origen == "C" and medida_destino == "K":
#         resultado = valor + 273.15
#     elif medida_origen == "F" and medida_destino == "C":
#         resultado = (valor - 32) * 5/9
#     elif medida_origen == "F" and medida_destino == "K":
#         resultado = (valor + 459.67) * 5/9
#     elif medida_origen == "K" and medida_destino == "C":
#         resultado = valor - 273.15
#     elif medida_origen == "K" and medida_destino == "F":
#         resultado = (valor * 9/5) - 459.67
#     else:
#         resultado = valor  # Si las medidas son iguales, no se realiza conversión
#     return resultado

# # # Ejemplo de uso
# # valor = 30
# # medida_origen = "C"
# # medida_destino = "F"
# # resultado = convertir_temperatura(valor, medida_origen, medida_destino)
# # print(f"{valor}{medida_origen} equivale a {resultado}{medida_destino}")

# # #Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer una impresión para cada combinación de los mismos:

# # combinaciones = [("C", "F"), ("C", "K"), ("F", "C"), ("F", "K"), ("K", "C"), ("K", "F")]

# # valor = 30

# #  for medida_origen, medida_destino in combinaciones:
# #     resultado = convertir_temperatura(valor, medida_origen, medida_destino)
# #      print(f"{valor}{medida_origen} equivale a {resultado}{medida_destino}")


# # #Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar un parámetro un número no entero o negativo

# def factorial(numero):
#     if not isinstance(numero, int) or numero < 0:
#         return None  # Devolver None si el número no es entero o es negativo
#     resultado = 1
#     for i in range(2, numero + 1):
#         resultado *= i
#     return resultado

# # # Ejemplo de uso
# # numero = 5
# # factorial_resultado = factorial(numero)
# # if factorial_resultado is not None:
# #     print(f"El factorial de {numero} es: {factorial_resultado}")
# # else:
# #     print("El número debe ser un entero no negativo")




# ############################################################################################
# ######################  CLASES  Y POO  ###############################

# # Crear la clase vehículo que contenga los atributos:
# # Color
# # Si es moto, auto, camioneta ó camión
# # Cilindrada del motor

# # class Vehiculo:
# #     def __init__(self, color, tipo, cilindrada):
# #         self.color = color
# #         self.tipo = tipo
# #         self.cilindrada = cilindrada



# # class Vehiculo:
# #     def __init__(self, color, tipo, cilindrada):
# #         self.color = color
# #         self.tipo = tipo
# #         self.cilindrada = cilindrada

# #A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:Acelerar
# #Frenar
# #Doblar

# class Vehiculo:
#     def __init__(self, color, tipo, cilindrada):
#         self.color = color
#         self.tipo = tipo
#         self.cilindrada = cilindrada
#         self.velocidad = 0

#     def acelerar(self, cantidad):
#         self.velocidad += cantidad

#     def frenar(self, cantidad):
#         self.velocidad -= cantidad

#     def doblar(self, direccion):
#         print(f"Girando hacia {direccion}")

# # Ejemplo de uso
# vehiculo1 = Vehiculo("Rojo", "Auto", 2000)
# vehiculo1.acelerar(50)
# print(f"Velocidad actual: {vehiculo1.velocidad}")
# vehiculo1.frenar(20)
# print(f"Velocidad actual: {vehiculo1.velocidad}")
# vehiculo1.doblar("izquierda")


# #Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
# # a1 = Vehiculo('rojo', 'auto', 2)
# # a2 = Vehiculo('blanco', 'camioneta', 3.6)
# # a3 = Vehiculo('negro', 'moto', 1)
# # a1.Acelerar(40)
# # a2.Acelerar(60)
# # a3.Acelerar(30)
# # a1.Doblar(30)
# # a3.Doblar(-30)
# # a2.Frenar(-50)


# class Vehiculo:
#     def __init__(self, color, tipo, cilindrada):
#         self.color = color
#         self.tipo = tipo
#         self.cilindrada = cilindrada
#         self.velocidad = 0

#     def acelerar(self, cantidad):
#         self.velocidad += cantidad

#     def frenar(self, cantidad):
#         self.velocidad -= cantidad

#     def doblar(self, angulo):
#         print(f"Girando {angulo} grados")

# # Instanciar objetos de la clase Vehiculo
# a1 = Vehiculo('rojo', 'auto', 2)
# a2 = Vehiculo('blanco', 'camioneta', 3.6)
# a3 = Vehiculo('negro', 'moto', 1)

# # Ejecutar métodos en cada objeto
# a1.acelerar(40)
# a2.acelerar(60)
# a3.acelerar(30)
# a1.doblar(30)
# a3.doblar(-30)
# a2.frenar(-50)

# # Imprimir el resultado
# print(f"Color: {a1.color}, Tipo: {a1.tipo}, Velocidad: {a1.velocidad}")
# print(f"Color: {a2.color}, Tipo: {a2.tipo}, Velocidad: {a2.velocidad}")
# print(f"Color: {a3.color}, Tipo: {a3.tipo}, Velocidad: {a3.velocidad}")


# #Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# class Vehiculo:
#     def __init__(self, color, tipo, cilindrada):
#         self.color = color
#         self.tipo = tipo
#         self.cilindrada = cilindrada
#         self.velocidad = 0
#         self.direccion = ""

#     def acelerar(self, cantidad):
#         self.velocidad += cantidad

#     def frenar(self, cantidad):
#         self.velocidad -= cantidad

#     def doblar(self, direccion):
#         self.direccion = direccion

#     def mostrar_estado(self):
#         print(f"Velocidad: {self.velocidad} km/h, Dirección: {self.direccion}")

#     def mostrar_info(self):
#         print(f"Color: {self.color}, Tipo: {self.tipo}, Cilindrada: {self.cilindrada}")

# # Ejemplo de uso
# vehiculo1 = Vehiculo("Rojo", "Auto", 2000)
# vehiculo1.acelerar(50)
# vehiculo1.doblar("Izquierda")
# vehiculo1.mostrar_estado()
# vehiculo1.mostrar_info()


# #Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6
# # Verificar Primo
# # Valor modal
# # Conversión grados
# # Factorial

# class Utilidades:
#     @staticmethod
#     def verificar_primo(numero):
#         if es_primo(numero):
#             print(f"{numero} es un número primo")
#         else:
#             print(f"{numero} no es un número primo")

#     @staticmethod
#     def obtener_valor_modal(lista):
#         modal = valor_modal(lista)
#         print(f"El valor modal de la lista {lista} es: {modal}")

#     @staticmethod
#     def convertir_grados(valor, medida_origen, medida_destino):
#         resultado = convertir_temperatura(valor, medida_origen, medida_destino)
#         print(f"{valor}{medida_origen} equivale a {resultado}{medida_destino}")

#     @staticmethod
#     def calcular_factorial(numero):
#         resultado = factorial(numero)
#         if resultado is not None:
#             print(f"El factorial de {numero} es: {resultado}")
#         else:
#             print("El número debe ser un entero no negativo")

# # Ejemplo de uso
# utilidades = Utilidades()

# # Verificar si un número es primo
# utilidades.verificar_primo(17)

# # Obtener el valor modal de una lista
# #utilidades.obtener_valor_modal([5, 2, 3, 2, 5, 5])

# # Convertir grados
# utilidades.convertir_grados(30, "C", "F")

# # Calcular factorial
# utilidades.calcular_factorial(5)


# #Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se
# #  aplquen las funciones incorporadas

# class Utilidades:
#     def __init__(self, lista):
#         self.lista = lista

#     def verificar_primo(self, numero):
#         if es_primo(numero):
#             print(f"{numero} es un número primo")
#         else:
#             print(f"{numero} no es un número primo")

#     def obtener_valor_modal(self):
#         modal = valor_modal(self.lista)
#         print(f"El valor modal de la lista {self.lista} es: {modal}")

#     def convertir_grados(self, valor, medida_origen, medida_destino):
#         resultado = convertir_temperatura(valor, medida_origen, medida_destino)
#         print(f"{valor}{medida_origen} equivale a {resultado}{medida_destino}")

#     def calcular_factorial(self, numero):
#         resultado = factorial(numero)
#         if resultado is not None:
#             print(f"El factorial de {numero} es: {resultado}")
#         else:
#             print("El número debe ser un entero no negativo")

# # Ejemplo de uso
# lista_numeros = [5, 2, 3, 2, 5, 5]
# utilidades = Utilidades(lista_numeros)

# # Verificar si un número es primo
# utilidades.verificar_primo(17)

# # Obtener el valor modal de la lista
# #utilidades.obtener_valor_modal()

# # Convertir grados
# utilidades.convertir_grados(30, "C", "F")

# # Calcular factorial
# utilidades.calcular_factorial(5)


# #Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar
# #  la importación del módulo y probar alguna de sus funciones


from utilidades import Utilidades

# # Ejemplo de uso
lista_numeros = [-5,'A',2, 3, 2, 5, 5]
utilidades = Utilidades(lista_numeros)

# # Verificar si un número es primo
#utilidades.verificar_primo('A')

# # Obtener el valor modal de la lista
# #utilidades.obtener_valor_modal()

# # Convertir grados
utilidades.convertir_grados(30, "J", "F")

# # Calcular factorial
# utilidades.calcular_factorial(5)


#############################################################################################
####################  ERRORES #######################

#Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código 
#pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de 
#números enteros pero ¿qué pasa si se envía otro tipo de dato?


# class Utilidades:
#     def __init__(self, lista):
#         if not isinstance(lista, list):
#             raise ValueError("Se esperaba una lista de números")
#         if not all(isinstance(num, int) for num in lista):
#             raise ValueError("La lista debe contener solo números enteros")
        
#         self.lista = lista

    # Resto de los métodos...


#En la función que hace la conversión de grados, validar que los parámetros enviados 
# sean los esperados, de no serlo, informar correctamente son los valores esperados.

# class Utilidades:
#     # Resto del código de la clase...
    
#     def convertir_grados(self, valor, medida_origen, medida_destino):
#         medidas_validas = ["C", "F", "K"]

#         if not isinstance(valor, (int, float)):
#             raise ValueError("El valor debe ser numérico")
#         if medida_origen not in medidas_validas:
#             raise ValueError("La medida de origen no es válida")
#         if medida_destino not in medidas_validas:
#             raise ValueError("La medida de destino no es válida")

        # Resto de la lógica de la función...



# Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2
#Creacion del objeto incorrecto
#Creacion correcta del objeto
#Metodo valor_modal()

# import unittest
# from utilidades import Utilidades

# class UtilidadesTestCase(unittest.TestCase):
#     def test_creacion_objeto_incorrecto(self):
#         with self.assertRaises(ValueError):
#             utilidades = Utilidades("no es una lista")

#     def test_creacion_objeto_correcto(self):
#         lista_numeros = [5, 2, 3, 2, 5, 5]
#         utilidades = Utilidades(lista_numeros)
#         self.assertIsInstance(utilidades, Utilidades)
#         self.assertEqual(utilidades.lista, lista_numeros)

#     def test_valor_modal(self):
#         lista_numeros = [5, 2, 3, 2, 5, 5]
#         utilidades = Utilidades(lista_numeros)
#         modal = utilidades.valor_modal()
#         self.assertEqual(modal, 5)

# if __name__ == '__main__':
#     unittest.main()

#Agregar casos de pruebas para el método conversion_grados()

# import unittest
# from utilidades import Utilidades

# class UtilidadesTestCase(unittest.TestCase):
#     def test_conversion_grados_celsius_a_fahrenheit(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.convertir_grados(25, "C", "F")
#         self.assertEqual(resultado, 77.0)

#     def test_conversion_grados_fahrenheit_a_celsius(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.convertir_grados(77, "F", "C")
#         self.assertEqual(resultado, 25.0)

#     def test_conversion_grados_celsius_a_kelvin(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.convertir_grados(25, "C", "K")
#         self.assertEqual(resultado, 298.15)

#     def test_conversion_grados_kelvin_a_fahrenheit(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.convertir_grados(298.15, "K", "F")
#         self.assertAlmostEqual(resultado, 77.0, places=1)

#     # Otros casos de prueba...

# if __name__ == '__main__':
#     unittest.main()

#Agregar casos de pruebas para el método factorial()

# def test_factorial_numero_positivo(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.factorial(5)
#         self.assertEqual(resultado, 120)

#     def test_factorial_numero_cero(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.factorial(0)
#         self.assertEqual(resultado, 1)

#     def test_factorial_numero_negativo(self):
#         utilidades = Utilidades([])
#         resultado = utilidades.factorial(-5)
#         self.assertIsNone(resultado)



#########################################################################################
#########################  manejo archivos  

#Crear un script con el nombre "clase09_ej1.py" que reciba 3 parámetros a elección, 
# verificando que sean exactamente esa cantidad, y muestre como salida
#  los parámetros recibidos

# import sys

# def main():
#     # Verificar la cantidad de parámetros
#     if len(sys.argv) != 4:
#         print("Error: Se esperan exactamente 3 parámetros.")
#         return

#     # Obtener los parámetros
#     parametro1 = sys.argv[1]
#     parametro2 = sys.argv[2]
#     parametro3 = sys.argv[3]

#     # Mostrar los parámetros recibidos
#     print("Parámetro 1:", parametro1)
#     print("Parámetro 2:", parametro2)
#     print("Parámetro 3:", parametro3)

# if __name__ == "__main__":
#     main()


# Para ejecutar el script, asegúrate de que el archivo "clase09_ej1.py" esté en el mismo directorio y, desde la línea de comandos, ejecuta el siguiente comando:

# Copy code
# python clase09_ej1.py valor1 valor2 valor3
# Reemplaza "valor1", "valor2" y "valor3" por los valores que desees pasar como parámetros. El script mostrará los parámetros recibidos en la salida.

# Por ejemplo, si ejecutas:

# graphql
# Copy code
# python clase09_ej1.py hola 42 True


#Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de 
# temperatura en grados centígrados, un valor de humedad y por último si llovio 
# (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto
#  "clase09_ej2.csv" una marca de tiempo y 
# esa información.

# 

#python clase09_ej2.py 25 60 True   #para ejecutar


#Crear un archivo a partir de los datos presentes en el diccionario provisto. El cual debe contener en la primera fila el nombre de las claves y luego cada línea los elementos i-ésimos de las listas de valores contiguos y separados por coma ','. Este archivo debe llamarse clase09_ej3.csv
# montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
#                         'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
#             'orden':[1,2,3,4,5,6,7,8,9,10],
#             'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
#                         ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
#             'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
#                     'Pakistán','Nepal'],
#             'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}


# 

# 

#Crear una carpeta llamada clase09_montañas_altas

#Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia os.system

#Listar el contenido de la carpeta clase09_montañas_altas

# import os

# # Crear la carpeta "clase09_montañas_altas"
# os.makedirs("clase09_montañas_altas", exist_ok=True)

# # Copiar el archivo "clase09_ej3.csv" en la carpeta "clase09_montañas_altas"
# os.system("cp clase09_ej3.csv clase09_montañas_altas/")

# # Listar el contenido de la carpeta "clase09_montañas_altas"
# contenido = os.listdir("clase09_montañas_altas")

# print("Contenido de la carpeta 'clase09_montañas_altas':")
# for archivo in contenido:
#     print(archivo)
