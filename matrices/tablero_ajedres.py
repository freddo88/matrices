def crear_tablero_ajedrez(tamano=8):
    tablero_local = []
    for fila in range(tamano):
        tablero_local.append([])
        for columna in range(tamano):
            if (fila + columna) % 2 == 0:
                tablero_local[fila].append('⬜')  # Blanco
            else:
                tablero_local[fila].append('⬛')  # Negro
    return tablero_local


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


if __name__ == "__main__":
    tablero = crear_tablero_ajedrez()
    imprimir_tablero(tablero)
