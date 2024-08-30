def winlose(board):
    """
    Descripción:
        Función que recibe el tablero del tictactoe y verifica si una de las dos fichas ganó.

        Retorna True o False, donde True indica victoria y False indica que el juego sigue
    """

    for i in range(0,3):
        if board[i][i] != " ":
            if i == 0:
                if board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0] or board[0][0] == board[1][1] == board[2][2]:
                    return True
            
            elif i == 1:
                if board[1][1] == board[0][1] == board[2][1] or board[1][1] == board[1][0] == board[1][2] or board[1][1] == board[0][2] == board[2][0]:
                    return True
                
            else:
                if board[2][2] == board[1][2] == board[0][2] or board[2][2] == board[2][1] == board[2][0]:
                    return True
    
    return False



# 0 1 2
# 3 4 5
# 6 7 8

# 0,0 0,1 0,2
# 1,0 1,1 1,2
# 2,0 2,1 2,2