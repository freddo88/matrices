🧩 Generador de Tablero de Ajedrez en Consola
Este proyecto en Python genera e imprime un tablero de ajedrez en la consola utilizando caracteres Unicode para representar las casillas blancas y negras.

📌 Descripción
El programa crea un tablero de ajedrez de tamaño configurable (por defecto, 8x8) y lo imprime en la terminal. Utiliza dos funciones principales:

crear_tablero_ajedrez(tamano=8): genera la estructura del tablero.

imprimir_tablero(tablero): imprime el tablero en formato visual.

Cada celda se representa con los siguientes símbolos:

⬜ Casilla blanca

⬛ Casilla negra

🧠 ¿Cómo funciona?
crear_tablero_ajedrez(tamano)

Crea una lista bidimensional (tablero) que representa las filas y columnas del tablero.

Recorre cada fila y columna.

Alterna los colores de las casillas usando la condición (fila + columna) % 2.

Si la suma es par, coloca una casilla blanca (⬜).

Si la suma es impar, coloca una casilla negra (⬛).

imprimir_tablero(tablero)

Recorre cada fila de la lista y las imprime unidas por espacios para simular el aspecto visual de un tablero de ajedrez.

Bloque principal (if **name** == "**main**")

Llama a las funciones para crear e imprimir el tablero cuando el archivo se ejecuta directamente.

▶️ Ejecución
Para ejecutar el programa, guarda el código en un archivo llamado por ejemplo tablero_ajedrez.py, y luego ejecútalo con Python:

python tablero_ajedrez.py
📦 Ejemplo de salida

⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
🛠️ Requisitos
Python 3.x

💡 Personalización
Puedes cambiar el tamaño del tablero pasando un valor diferente al llamar la función:
python
tablero = crear_tablero_ajedrez(6)
