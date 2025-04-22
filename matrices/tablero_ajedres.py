def crear_tablero_ajedrez(tamano=8):
    tablero = []
    for fila in range(tamano):
        tablero.append([])
        for columna in range(tamano):
            if (fila + columna) % 2 == 0:
                tablero[fila].append('⬜')  # Blanco
            else:
                tablero[fila].append('⬛')  # Negro
    return tablero


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


if __name__ == "__main__":
    tablero = crear_tablero_ajedrez()
    imprimir_tablero(tablero)
