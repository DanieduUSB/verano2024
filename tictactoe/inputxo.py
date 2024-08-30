import time

def inpxo(board,turn):
    """
    Descripción:
        Función que recibe el tablero del tictactoe y el turno actual. Permite al usuario ingresar
        un input para colocar su ficha, y verifica si el espacio donde intenta colocar la ficha esta
        libre u ocupado.

        Retorna el tablero del tictactoe con la nueva ficha, la cual será "X" u "O" dependiendo del
        turno
    """

    if turn == 0:
        print("Es el turno de las X")
    else:
        print("Es el turno de las O")

    time.sleep(0.75)

    print("[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]")

    n = int(input('Escribe un número del 1 al 9 para elegir en que casilla poner la ficha: '))
    # Permite al usuario ingresar un valor numérico

    time.sleep(0.5)

    if n in range(1,10):
    # Verifica si el valor numérico esta entre el 1 y el 9
        i = int((n-1)/3)
        j = (n-1) % 3
        # define "i" y "j" para poder acceder a la casilla correspondiente elegida por el usuario

        if board[i][j] == " ":
        # Verifica si el espacio dentro de la lista que funciona como el tablero del tictactoe esta
        # vació
  
            if turn == 0:
                board[i][j] = "X"
                return board
            # Si es el turno de las X, el espacio del tablero que eligió el usuario cambia a X,
            # y la función retorna el nuevo tablero

            else:
                board[i][j] = "O"
                return board
            # Si es el turno de las C, el espacio del tablero que eligió el usuario cambia a C,
            # y la función retorna el nuevo tablero
        
        else:
            print("Ese espacio ya tiene otra ficha, elige otro")
            inpxo(board,turn)
        # Si el espacio del tablero no esta vacío, vuelve a ejecutar la función con los mismos
        # valores para que el usuario elija otro espacio para poner su ficha

    else:
        print("Debes elegir un número del 1 al 9")
        inpxo(board,turn)
    # Si el número elegido no está en el rango 1 a 9, vuelve a ejecutar la función con los mismos
    # valores para que el usuario elija un espacio para poner su ficha