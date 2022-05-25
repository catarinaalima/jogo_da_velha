"""
Estácio de Sá
Nome: Iara Catarina Silva e Lima
"""
from tkinter import *
from tkinter import messagebox

# Inicio da Classe
class TipTapToe( Frame ):
    """
    Metodo construtor da Classe.
    Define os elementos da janela principal e inicia o programa
    """
    def __init__(self):
        # Cria nossa janela principal.
        self.__janela = Tk()
        self.__janela.title('Jogo da velha - Trabalho')

        # Inicializa algumas variaveis de controle.
        self.__rodada_jogador = 1                       # controla de quem e a rodada
        self.__label_clicada = ""                       # guada o valor da label clicada
        self.__possibilidades = list(range(1, 10))      # gera uma lista para controlar a marcacao do jogo
        self.__ganhou = False                   # guarda o status da jogada


        # Cria os frames do jogo.
        self.__frame_placar = Frame(self.__janela, bg="white", height=100, width=400)
        self.__frame_tabuleiro = Frame(self.__janela, bg="yellow", height=250, width=400)
        self.__frame_info = Frame(self.__janela, bg="black", height=100, width=400)

        # Monta o frame 1 - Placar.
        self.__label_p1 = Label(self.__frame_placar, text='P1 ', font=('Avantgarde', 32), fg='purple')
        self.__pontos_p1 = StringVar()
        self.__pontos_p1.set("0")
        self.__placar_p1 = Label(self.__frame_placar, width=2, font=('Avantgarde', 32), fg='white', bg='black', textvariable=self.__pontos_p1, justify='center')

        self.__label_versus = Label(self.__frame_placar, text='x', font=('Avantgarde', 32), fg='black', width=6)

        self.__label_p2 = Label(self.__frame_placar, text=' P2', font=('Avantgarde', 32), fg='purple')
        self.__pontos_p2 = StringVar()
        self.__pontos_p2.set("0")
        self.__placar_p2 = Label(self.__frame_placar, width=2, font=('Avantgarde', 32), fg='white', bg='black', textvariable=self.__pontos_p2, justify='center')

        # Organiza widgets do placar na grid.
        self.__label_p1.grid(row=0, column=0, sticky=W)
        self.__placar_p1.grid(row=0, column=1, sticky=W)
        self.__label_versus.grid(row=0, column=2, sticky=W)
        self.__placar_p2.grid(row=0, column=3, sticky=W)
        self.__label_p2.grid(row=0, column=4, sticky=W)

        # Monta o frame 2 - tabuleiro do jogo.
        # Variaveis das labels que são alteradas dinamicamente ao se clicar na label.
        self.__char_pos_1 = StringVar()
        self.__char_pos_2 = StringVar()
        self.__char_pos_3 = StringVar()
        self.__char_pos_4 = StringVar()
        self.__char_pos_5 = StringVar()
        self.__char_pos_6 = StringVar()
        self.__char_pos_7 = StringVar()
        self.__char_pos_8 = StringVar()
        self.__char_pos_9 = StringVar()

        # Labels que formam o tabuleiro do jogo.
        self.__label_pos_1 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_1)
        self.__label_pos_2 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_2)
        self.__label_pos_3 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_3)
        self.__label_pos_4 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_4)
        self.__label_pos_5 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_5)
        self.__label_pos_6 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_6)
        self.__label_pos_7 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_7)
        self.__label_pos_8 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_8)
        self.__label_pos_9 = Label(self.__frame_tabuleiro, font=('Avantgarde', 32), text=' ', width=6, justify='center', relief='groove', height='2', textvariable=self.__char_pos_9)

        # Cria o vinculo das labels a uma funcão com o evento "clique do 1º botao do mouse".
        self.__label_pos_1.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_2.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_3.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_4.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_5.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_6.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_7.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_8.bind("<Button-1>", self.__marcar_opcao)
        self.__label_pos_9.bind("<Button-1>", self.__marcar_opcao)

        # Organiza widgets do tabuleiro na grid.
        self.__label_pos_1.grid(row=0, column=0, sticky=W)
        self.__label_pos_2.grid(row=0, column=1, sticky=W)
        self.__label_pos_3.grid(row=0, column=2, sticky=W)
        self.__label_pos_4.grid(row=1, column=0, sticky=W)
        self.__label_pos_5.grid(row=1, column=1, sticky=W)
        self.__label_pos_6.grid(row=1, column=2, sticky=W)
        self.__label_pos_7.grid(row=2, column=0, sticky=W)
        self.__label_pos_8.grid(row=2, column=1, sticky=W)
        self.__label_pos_9.grid(row=2, column=2, sticky=W)

        # Monta o frame 3 - rodapé.
        # Variavel dinâmica para guardar as mensagens da jogada no rodapé.
        self.__var_info = StringVar()
        self.__var_info.set('Rodada do Jogador 1')

        # Label do rodapé.
        self.__label_info = Label(self.__frame_info, font=('Avantgarde', 15), textvariable=self.__var_info, justify='center', bg='black', fg='purple', width='45', pady='10')
        self.__label_info.pack(fill=X, expand=1)

        # Empacota os frames na janela principal.
        self.__frame_placar.pack()
        self.__frame_tabuleiro.pack()
        self.__frame_info.pack()

        # Criando um loop eterno (basicamente um "while True" por debaixo dos panos pra abrir nossa janela).
        self.__janela.mainloop()

    """
    Metodo responsável por mostrar a marcação do jogador no tabuleiro ao clicar nele.    
    """
    def __marcar_opcao(self, event):
        # Pega o label clicado pelo jogador.
        self.__label_clicada = event.widget.winfo_name()

        # Estes blocos verificam qual label foi clicada pelo jogador, marcando "x" ou "o" de acordo com o jogador da rodada.
        # Também guarda a opcao na lista de jogadas que e usada para ver se há uma jogada vencedora.
        # Por fim, altera a cor do texto de acordo com o jogador da rodada ("x" sempre vermelho e "o" sempre azul).
        if self.__label_clicada == '!label' and self.__char_pos_1.get() == '':
            self.__char_pos_1.set('X') if self.__rodada_jogador == 1 else self.__char_pos_1.set('O')
            self.__possibilidades[0] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_1.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_1.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label2' and self.__char_pos_2.get() == '':
            self.__char_pos_2.set('X') if self.__rodada_jogador == 1 else self.__char_pos_2.set('O')
            self.__possibilidades[1] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_2.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_2.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label3' and self.__char_pos_3.get() == '':
            self.__char_pos_3.set('X') if self.__rodada_jogador == 1 else self.__char_pos_3.set('O')
            self.__possibilidades[2] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_3.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_3.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label4' and self.__char_pos_4.get() == '':
            self.__char_pos_4.set('X') if self.__rodada_jogador == 1 else self.__char_pos_4.set('O')
            self.__possibilidades[3] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_4.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_4.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label5' and self.__char_pos_5.get() == '':
            self.__char_pos_5.set('X') if self.__rodada_jogador == 1 else self.__char_pos_5.set('O')
            self.__possibilidades[4] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_5.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_5.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label6' and self.__char_pos_6.get() == '':
            self.__char_pos_6.set('X') if self.__rodada_jogador == 1 else self.__char_pos_6.set('O')
            self.__possibilidades[5] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_6.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_6.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label7' and self.__char_pos_7.get() == '':
            self.__char_pos_7.set('X') if self.__rodada_jogador == 1 else self.__char_pos_7.set('O')
            self.__possibilidades[6] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_7.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_7.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label8' and self.__char_pos_8.get() == '':
            self.__char_pos_8.set('X') if self.__rodada_jogador == 1 else self.__char_pos_8.set('O')
            self.__possibilidades[7] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_8.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_8.config(fg='white')
            self.__verifica_se_ganhou()
        elif self.__label_clicada == '!label9' and self.__char_pos_9.get() == '':
            self.__char_pos_9.set('X') if self.__rodada_jogador == 1 else self.__char_pos_9.set('O')
            self.__possibilidades[8] = 'X' if self.__rodada_jogador == 1 else 'O'
            self.__label_pos_9.config(fg='black') if self.__rodada_jogador == 1 else self.__label_pos_9.config(fg='white')
            self.__verifica_se_ganhou()

    """
    Metodo responsável por verificar se ja há uma jogada vencedora.    
    """
    def __verifica_se_ganhou(self):

        # Define as possibilidades para vencer uma rodada. Inicialmente todas as possibilidades são falsas.
        # Quando temos uma jogada vencedora, a variavel desta sequencia recebe True.
        game1 = self.__possibilidades[0] == self.__possibilidades[1] == self.__possibilidades[2] # primeira linha
        game2 = self.__possibilidades[3] == self.__possibilidades[4] == self.__possibilidades[5] # segunda linha
        game3 = self.__possibilidades[6] == self.__possibilidades[7] == self.__possibilidades[8] # terceira linha
        game4 = self.__possibilidades[0] == self.__possibilidades[3] == self.__possibilidades[6] # primeira coluna
        game5 = self.__possibilidades[1] == self.__possibilidades[4] == self.__possibilidades[7] # segunda coluna
        game6 = self.__possibilidades[2] == self.__possibilidades[5] == self.__possibilidades[8] # terceira coluna
        game7 = self.__possibilidades[0] == self.__possibilidades[4] == self.__possibilidades[8] # primeira diagonal
        game8 = self.__possibilidades[2] == self.__possibilidades[4] == self.__possibilidades[6] # segunda diagonal

        # Verifica se ainda há jogadas disponiveis.
        continua_jogo = False
        for valor in self.__possibilidades:
            if str(valor).isdigit():
                continua_jogo = True

        # Adiciona estas possibilidades numa lista.
        checaGames = [game1, game2, game3, game4, game5, game6, game7, game8]

        # Itera a lista para verificar se há uma rodada vitoriosa (True).
        for possibilidade in checaGames:
            if possibilidade:
               self.__ganhou = True

        # Se encontrar uma possibilidade vitoriosa, chama a funcão para declarar o vencedor.
        # Caso contrário, altera o turno para o outro jogador e continua o jogo.
        if self.__ganhou:
            self.__jogador_ganhou()
        else:
            if continua_jogo: # Se ainda há jogadas disponiveis, continua o jogo.
                self.__altera_rodada()
            else:             # Se não tiver mais jogadas, houve um empate.
                titulo = 'EMPATE!'
                mensagem = 'Opa, espera ai. Parece que temos um empate.\nQue tal mais uma rodada?'
                self.__mostra_caixa_dialogo(titulo, mensagem)


    """
    Metodo chamado quando um jogador ganha a partida.   
    """
    def __jogador_ganhou(self):
        self.__ganhou = True
        titulo = 'Parabéns!'
        mensagem = 'O Jogador ' + str(self.__rodada_jogador) + ' venceu! \nQue tal mais uma rodada?'
        self.__marcar_ponto()
        self.__mostra_caixa_dialogo(titulo, mensagem)



    """
    Metodo responsável por marcar o ponto no placar do jogador vencedor.    
    """
    def __marcar_ponto(self):
        if self.__rodada_jogador == 1:
            valor = int(self.__pontos_p1.get())
            valor = valor + 1
            self.__pontos_p1.set(valor)
        elif self.__rodada_jogador == 2:
            valor = int(self.__pontos_p2.get())
            valor = valor + 1
            self.__pontos_p2.set(valor)


    """
    Metodo responsável por alterar a rodada entre os jogadores.   
    """
    def __altera_rodada(self):
        if self.__rodada_jogador == 1:
            self.__rodada_jogador = 2
            self.__var_info.set('Rodada do Jogador 2')
        else:
            self.__rodada_jogador = 1
            self.__var_info.set('Rodada do Jogador 1')


    """
    Metodo responsavel por exibir a caixa de dialogo no final das partidas.   
    """
    def __mostra_caixa_dialogo(self, titulo, mensagem):
        # Altera a mensagem de informacao do Rodapé.
        self.__var_info.set(mensagem)

        # Exibe a caixa de dialogo e recebe a opcao escolhida pelos jogadores (True ou False).
        resp = messagebox.askretrycancel(title=titulo, message=mensagem)

        # Se o jogador escolher "Repetir", reinicia o jogo. Se escolher cancelar, fecha o jogo.
        if resp:
            self.__reiniciar_joog()
        else:
            self.__janela.quit()

    """
    Metodo que reinicia a partida, zerando as variaveis para uma nova rodada.   
    """
    def __reiniciar_joog(self):
        # Recria a lista de possibilidades.
        self.__possibilidades = list(range(1, 10))
        self.__ganhou = False

        # Verifica o jogador que ganhou para alterar a info e iniciar a partida a partir dele.
        if self.__rodada_jogador == 1:
            self.__var_info.set('Rodada do Jogador 1')
        else:
            self.__var_info.set('Rodada do Jogador 2')

        # Limpa o tabuleiro com as marcações "x" e "o".
        self.__char_pos_1.set('')
        self.__char_pos_2.set('')
        self.__char_pos_3.set('')
        self.__char_pos_4.set('')
        self.__char_pos_5.set('')
        self.__char_pos_6.set('')
        self.__char_pos_7.set('')
        self.__char_pos_8.set('')
        self.__char_pos_9.set('')

# FIM DA CLASSE TIPTAPTOE
"""
Referências --> https://bastter.com/mercado/forum/863423/
extra-4--python--modo-multiplayer--criando-um-jogo-da-velha-pra-jogar-com-os-pimpolhos-pt2
"""
# Instancia a classe e inicia o jogo! LET'S PLAY!
TipTapToe()