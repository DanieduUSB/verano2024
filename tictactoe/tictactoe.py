import time
from inputxo import inpxo
from verify import winlose

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print(f"{board[0]}")
print(f"{board[1]}")
print(f"{board[2]}")
# Tablero vacío al inicio del juego

time.sleep(0.5)


def tictactoe(t):
    """
    Descripción:
        Función principal del tictactoe. Recibe una variable t la cual determina el turno de los jugadores,
        organiza el resto de funciones para que se ejecuten en el momento debido. Se ejecuta nuevamente si
        el juego no ha terminado
    """

    inpxo(board,t)

    time.sleep(0.25)

    print(f"{board[0]}")
    print(f"{board[1]}")
    print(f"{board[2]}")

    time.sleep(0.50)

    if winlose(board):
        if t == 0:
            print("Ganan las X")
            return
        else:
            print("Ganan las O")
            return
    
    else:

        for fila in range(0,3):
            for columna in range(0,3):
                if board[fila][columna] == " ":
                    if t == 0:
                        tictactoe(1)
                        return
                    else:
                        tictactoe(0)
                        return
                
                elif fila == columna == 2:
                    print("Gana la vieja")
                    return

tictactoe(0)



