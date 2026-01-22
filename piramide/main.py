def piramide(a):
    # Bucle principal: controla la cantidad de filas de la pirámide
    # b va desde 1 hasta 'a'
    for b in range(1, a + 1):

        # Este bucle imprime los espacios en blanco a la izquierda
        # Sirven para centrar la pirámide
        # A medida que b aumenta, los espacios disminuyen
        for c in range(a - b):
            print(" ", end="")

        # Este bucle imprime los asteriscos (*)
        # La cantidad de asteriscos es impar: 1, 3, 5, 7, ...
        # Se usa 2*b - 1 (pero range llega hasta 2*b)
        for d in range(1, 2 * b):
            print("*", end="")

        # Salto de línea para pasar a la siguiente fila
        print()

# Llamada a la función
# Imprime una pirámide de 6 niveles
piramide(6)
