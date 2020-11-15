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
        for i in range(len(self.matriz_tabuleiro)):
            v = []
            for j in range(len(self.matriz_tabuleiro[i])):
                if self.matriz_tabuleiro[i][j] == 'b':
                    x = 95*j
                    v.append(Peca('preta', x, 100))
                if self.matriz_tabuleiro[i][j] == 'a':
                    x = 95*j
                    v.append(Peca('branca', x, 200))
                else:
                    v.append('_')
            matriz.append(v)
            v = []

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j]!= '_':
                    screen.blit(matriz[i][j].getImg(), (matriz[i][j].x, matriz[i][j].y))

        #tamanho = 8

        #for i in range(tamanho):
        #black = pygame.image.load('img/black.png')
        #black = pygame.transform.scale(black, (50,50))
        #black_rect = black.get_rect()
        #black_rect.y = 100


        #white = pygame.image.load('img/white.png')
        #white = pygame.transform.scale(white, (50,50))
        #white_rect = white.get_rect()
        #white_rect.y = 105

        
        #for i in range(len(self.matriz_tabuleiro)):
        #       black_rect.x = 92
        #       white_rect.x = 92
        #        for j in range(len(self.matriz_tabuleiro[i])):
        #            if self.matriz_tabuleiro[i][j] == 'b':
        #               screen.blit(black, black_rect)
        #            if self.matriz_tabuleiro[i][j] == 'a':
        #               screen.blit(white, white_rect)
        #            black_rect.x += 65
        #            white_rect.x += 65
        #    if(i%2!=0):
        #        black_rect.x = 90
        #        white_rect.x = 92
        #        for j in range(len(self.matriz_tabuleiro[i])):
        #            if self.matriz_tabuleiro[i][j] == 'b':
        #                screen.blit(black, black_rect)
        #            if self.matriz_tabuleiro[i][j] == 'a':
        #               screen.blit(white, white_rect)
        #            black_rect.x += 65
        #            white_rect.x += 65
    
        #   black_rect.y += 65
        #    white_rect.y += 65
        