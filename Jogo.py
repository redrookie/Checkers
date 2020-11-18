import pygame
import pygame_menu
from Peca import Peca


class Jogo:
    def __init__(self):
        self.status = 'Jogando'
        self.turno = 1
        self.jogadores = ('a', 'b')
        self.cedula_selecionada = None
        self.matriz_tabuleiro = [['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                                 ['b', '_', 'b', '_', 'b', '_', 'b', '_'],
                                 ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                                 ['_', '_', '_', '_', '_', '_', '_', '_'],
                                 ['_', '_', '_', '_', '_', '_', '_', '_'],
                                 ['_', 'a', '_', 'a', '_', 'a', '_', 'a'],
                                 ['a', '_', 'a', '_', 'a', '_', 'a', '_'],
                                 ['_', 'a', '_', 'a', '_', 'a', '_', 'a']]

    # Change deve usar o formato (x_antigo, y_antigo, x_novo, y_novo)
    def desenha_tabuleiro(self, screen, board):
        matriz = []
        y = 5
        for i in range(len(self.matriz_tabuleiro)):
            v = []
            for j in range(len(self.matriz_tabuleiro[i])):
                if self.matriz_tabuleiro[i][j] == '_':
                    v.append('_')
                if self.matriz_tabuleiro[i][j] == 'b':
                    x = self.getX(i, j)
                    v.append(Peca('preta', x, y))
                if self.matriz_tabuleiro[i][j] == 'a':
                    x = self.getX(i, j)
                    v.append(Peca('branca', x, y))

            y += 66
            matriz.append(v)
            v = []
            screen.blit(board, (0, 0))
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] != '_':
                        screen.blit(matriz[i][j].getImg(), (matriz[i][j].x, matriz[i][j].y))


    def getX(self, i, j):
        if i == 0 or i == 2 or i == 5 or i == 7:
            if j == 1:
                return 65
            if j == 3:
                return 195
            if j == 5:
                return 335
            if j == 7:
                return 465
        if i == 1 or i == 6:
            if j == 0:
                return 0
            if j == 2:
                return 135
            if j == 4:
                return 270
            if j == 6:
                return 400

    def movimenta_peca(self, screen, mouse_pos, board): # mouse_pos guarda as posicoes antiga e nova do mouse num array contendo 2 tuplas
        limite_posicoes = [56, 123, 189, 256, 325, 392, 460, 516] #Limite em pixels de cada quadrado em X e Y
        indice_antigo_superior_x = 0
        indice_antigo_superior_y = 0
        indice_novo_superior_x = 0
        indice_novo_superior_y = 0
        for i in range(8):
            if limite_posicoes[i] > mouse_pos[0][0]:
                indice_antigo_superior_x = i
                break
        for i in range(8):
            if limite_posicoes[i] > mouse_pos[1][0]:
                indice_antigo_superior_y = i
                break
        for i in range(8):
            if limite_posicoes[i] > mouse_pos[0][1]:
                indice_novo_superior_x = i
                break
        for i in range(8):
            if limite_posicoes[i] > mouse_pos[1][1]:
                indice_novo_superior_y = i
                break
        print(indice_antigo_superior_x)
        print(indice_antigo_superior_y)
        print(indice_novo_superior_x)
        print(indice_novo_superior_y)
        val_aux = self.matriz_tabuleiro[indice_novo_superior_x][indice_novo_superior_y] #Auxiliar para permitir o swap entre as posicoes da matriz
        self.matriz_tabuleiro[indice_novo_superior_x][indice_novo_superior_y] = self.matriz_tabuleiro[indice_antigo_superior_x][indice_antigo_superior_y]
        self.matriz_tabuleiro[indice_antigo_superior_x][indice_antigo_superior_y] = val_aux
        self.desenha_tabuleiro(screen, board)



