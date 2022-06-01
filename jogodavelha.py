# Importando RANDOM
import random

# Criando classe;
class JogoDaVelha:

    # Método construtor;
    def __init__(self):
        self.board = []

    def criando_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def primeiro_player(self):
        return random.randint(0, 1)

    def fixar_lugar(self, row, col, player):
        self.board[row][col] = player

    def player_ganhar(self, player):
        win = None

        n = len(self.board)

        # Checando linhas.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Checando colunas.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Checando diagonal.
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def passar_vez_player(self, player):
        return 'X' if player == 'O' else 'O'

    def mostrar_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.criando_board()

        player = 'X' if self.primeiro_player() == 1 else 'O'
        while True:
            print(f"Vez do {player}.")

            self.mostrar_board()

            # Pegando informação do usuário.
            row, col = list(
                map(int, input("Digite primeiramente uma linha e depois uma coluna com números, de acordo com o lugar que deseja (Exemplo --> 1 1): ").split()))
            print()

            # Fixando o lugar.
            self.fixar_lugar(row - 1, col - 1, player)

            # Checando se o jogador ganhou ou não.
            if self.player_ganhar(player):
                print(f"Player {player} ganhou o jogo!")
                break

            # Checando se foi jogado ou não.
            if self.is_board_filled():
                print("Empate!")
                break

            # Passando a vez.
            player = self.passar_vez_player(player)

        # Mostrando o final. 
        print()
        self.mostrar_board()

"""
 Referências: https://geekflare.com/tic-tac-toe-python-code/
"""

# Começando o jogo.
tic_tac_toe = JogoDaVelha()
tic_tac_toe.start()
