import pygame
import pygame_menu
from Peca import Peca


class Jogo:
    def __init__(self):
        self.status = 'Jogando'
        self.turno = 1
        self.jogadores = ('a', 'b')
        self.cedula_selecionada = None
        self.matriz_tabuleiro = [['_', 'b','_', 'b','_', 'b','_', 'b'],
                                 ['b','_','b','_', 'b', '_', 'b', '_'],
                                 ['_', 'b','_', 'b','_', 'b','_', 'b'],
                                 ['_','_','_','_', '_', '_', '_', '_'],
                                 ['_', '_','_', '_','_', '_','_', '_'],
                                 ['_','a','_','a', '_', 'a', '_', 'a'],
                                 ['a', '_','a', '_','a', '_','a', '_'],
                                 ['_','a','_','a', '_', 'a', '_', 'a']]

    def desenha_tabuleiro(self, screen):
        matriz = []
        y = 100
        for i in range(len(self.matriz_tabuleiro)):
            v = []
            for j in range(len(self.matriz_tabuleiro[i])):
                if self.matriz_tabuleiro[i][j]=='_':
                    v.append('_')
                if self.matriz_tabuleiro[i][j] == 'b':
                    x = 95*j
                    v.append(Peca('preta', x, y))
                if self.matriz_tabuleiro[i][j] == 'a':
                    x = 95*j
                    v.append(Peca('branca', x, y))
 
            y+= 65
            matriz.append(v)
            v = []

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j]!= '_':
                    screen.blit(matriz[i][j].getImg(), (matriz[i][j].x, matriz[i][j].y))
