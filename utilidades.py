def __init__(self, lista):
        if not isinstance(lista, list):
            raise ValueError("Se esperaba una lista de números")
        if not all(isinstance(num, int) for num in lista):
            raise ValueError("La lista debe contener solo números enteros")
        
        self.lista = lista
pass



def es_primo(numero):
    # Implementación de la función es_primo() aquí
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
pass

def valor_modal(self,lista,menor):
    # Implementación de la función valor_modal() aquí
     lista_unicos = []
     lista_repeticiones = []
     if len(lista) == 0:
            return None
     if (menor):
            lista.sort()
     else:
            lista.sort(reverse=True)
     for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
                moda = lista_unicos[0]
                maximo = lista_repeticiones[0]
     for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
            return moda, maximo
pass

def convertir_temperatura(valor, medida_origen, medida_destino):
    # Implementación de la función convertir_temperatura() aquí
      if medida_origen == "C" and medida_destino == "F":
        resultado = (valor * 9/5) + 32
      elif medida_origen == "C" and medida_destino == "K":
        resultado = valor + 273.15
      elif medida_origen == "F" and medida_destino == "C":
        resultado = (valor - 32) * 5/9
      elif medida_origen == "F" and medida_destino == "K":
        resultado = (valor + 459.67) * 5/9
      elif medida_origen == "K" and medida_destino == "C":
        resultado = valor - 273.15
      elif medida_origen == "K" and medida_destino == "F":
        resultado = (valor * 9/5) - 459.67
      else:
        resultado = valor  # Si las medidas son iguales, no se realiza conversión
      return resultado
pass

def factorial(numero):
    # Implementación de la función factorial() aquí
    if not isinstance(numero, int) or numero < 0:
        return None  # Devolver None si el número no es entero o es negativo
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado
    pass

class Utilidades:
    def __init__(self, lista):
        self.lista = lista

    def verificar_primo(self, numero):
        if es_primo(numero):
            print(f"{numero} es un número primo")
        else:
            print(f"{numero} no es un número primo")

    def obtener_valor_modal(self):
        modal = valor_modal(self.lista)
        print(f"El valor modal de la lista {self.lista} es: {modal}")

    def convertir_grados(self, valor, medida_origen, medida_destino):
        medidas_validas = ["C", "F", "K"]

        if not isinstance(valor, (int, float)):
            raise ValueError("El valor debe ser numérico")
        if medida_origen not in medidas_validas:
            raise ValueError("La medida de origen no es válida")
        if medida_destino not in medidas_validas:
            raise ValueError("La medida de destino no es válida")

        resultado = convertir_temperatura(valor, medida_origen, medida_destino)
        print(f"{valor}{medida_origen} equivale a {resultado}{medida_destino}")

    def calcular_factorial(self, numero):
        resultado = factorial(numero)
        if resultado is not None:
            print(f"El factorial de {numero} es: {resultado}")
        else:
            print("El número debe ser un entero no negativo")
