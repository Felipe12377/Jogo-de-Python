#python
# Jogo da Velha (Tic Tac Toe) em Python

# Tabulereiro representado por uma lista de 9 posições (incialmente vazias)
board = ['' for _ in range(9)]

def print_board():
    """
    Exibe o tabuleiro atual formatado com as marcações dos jogadores
    Formato: 
    | X | O | X |
    | O | X | O |
    | X | O | X |
    """

    # Cria cada linha do tabuleiro usando formatação de string
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])