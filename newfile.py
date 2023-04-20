while True:
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n > 0:
            break
        else:
            print("El número debe ser positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Debe ingresar un número entero. Inténtelo de nuevo.")

resultados = []
suma = 0
for i in range(1, n+1):
    termino = 1/i
    suma += termino
    resultados.append(suma)

print("La serie es:", end=" ")
for r in resultados:
    print("{:.2f}".format(r), end=" ")

