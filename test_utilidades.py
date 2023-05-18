import unittest
from utilidades import Utilidades

class UtilidadesTestCase(unittest.TestCase):
    # def test_creacion_objeto_incorrecto(self):
    #     with self.assertRaises(ValueError):
    #         utilidades = Utilidades("no es una lista")

    # def test_creacion_objeto_correcto(self):
    #     lista_numeros = [5, 2, 3, 2, 5, 5]
    #     utilidades = Utilidades(lista_numeros)
    #     self.assertIsInstance(utilidades, Utilidades)
    #     self.assertEqual(utilidades.lista, lista_numeros)

    # def test_valor_modal(self):
    #     lista_numeros = [5, 2, 3, 2, 5, 5]
    #     utilidades = Utilidades(lista_numeros)
    #     modal = utilidades.valor_modal()
    #     self.assertEqual(modal, 5)

    # def test_conversion_grados_celsius_a_fahrenheit(self):
    #     utilidades = Utilidades([])
    #     resultado = utilidades.convertir_grados(25, "C", "F")
    #     self.assertEqual(resultado, 77.0)

    # def test_conversion_grados_fahrenheit_a_celsius(self):
    #     utilidades = Utilidades([])
    #     resultado = utilidades.convertir_grados(77, "F", "C")
    #     self.assertEqual(resultado, 25.0)

    # def test_conversion_grados_celsius_a_kelvin(self):
    #     utilidades = Utilidades([])
    #     resultado = utilidades.convertir_grados(25, "C", "K")
    #     self.assertEqual(resultado, 298.15)

    # def test_conversion_grados_kelvin_a_fahrenheit(self):
    #     utilidades = Utilidades([])
    #     resultado = utilidades.convertir_grados(298.15, "K", "F")
    #     self.assertAlmostEqual(resultado, 77.0, places=1)

    def test_factorial_numero_positivo(self):
        utilidades = Utilidades([])
        resultado = utilidades.calcular_factorial(5)
        self.assertEqual(resultado, 120)

    def test_factorial_numero_cero(self):
        utilidades = Utilidades([])
        resultado = utilidades.calcular_factorial(0)
        self.assertEqual(resultado, 1)

    def test_factorial_numero_negativo(self):
        utilidades = Utilidades([])
        resultado = utilidades.calcular_factorial(-5)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
