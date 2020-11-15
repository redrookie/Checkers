import pygame


class Peca:
    def __init__(self, cor, x, y):
        self.cor = cor
        self.x = x
        self.y = y
        self.img = None
    
    def getImg(self):
        if self.cor == 'preta':
            self.img = pygame.image.load('img/black.png')
            self.img = pygame.transform.scale(self.img, (50,50))
            return self.img
        if self.cor == 'branca':
            self.img = pygame.image.load('img/white.png')
            self.img = pygame.transform.scale(self.img, (50,50))
            return self.img
            