# Programa para reservar un asiento en una sala de cine

# Crear una matriz de 3 filas y 4 columnas
# Todos los asientos comienzan libres con el valor 0
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar la fila al usuario
fila = int(input("Ingrese la fila que desea reservar (0 a 2): "))

# Solicitar la columna al usuario
columna = int(input("Ingrese la columna que desea reservar (0 a 3): "))

# Marcar el asiento seleccionado como reservado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

# Recorrer la matriz utilizando bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    
    # Salto de línea al terminar cada fila
    print()