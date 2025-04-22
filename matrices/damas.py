checkers_board = [
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    ['b', 0, 'b', 0, 'b', 0, 'b', 0],
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0],
    [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0]
]

print(checkers_board)
print(checkers_board[0][1])  # Imprime la pieza en la posición (0, 1)   # 'b'
print(checkers_board[0][1] == 0)  # False   # La posición (0, 1) no está vacía
# True   # La posición (0, 1) tiene una pieza negra
print(checkers_board[0][1] == 'b')
