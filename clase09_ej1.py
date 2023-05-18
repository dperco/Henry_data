import sys

def main():
    # Verificar la cantidad de parámetros
    if len(sys.argv) != 4:
        print("Error: Se esperan exactamente 3 parámetros.")
        return

    # Obtener los parámetros
    parametro1 = sys.argv[1]
    parametro2 = sys.argv[2]
    parametro3 = sys.argv[3]

    # Mostrar los parámetros recibidos
    print("Parámetro 1:", parametro1)
    print("Parámetro 2:", parametro2)
    print("Parámetro 3:", parametro3)

if __name__ == "__main__":
    main()
