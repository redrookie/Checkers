import pygame

class Peca(pygame.sprite.Sprite):

    def __init__(self, cor, pos):
        super().__init__()
        self.cor = cor
        self.pos = pos
        self.image = self.getImg()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def getImg(self):
        if self.cor == 'preta':
            self.img = pygame.image.load('img/black.png')
            self.img = pygame.transform.scale(self.img, (50,50))
            return self.img
        if self.cor == 'branca':
            self.img = pygame.image.load('img/white.png')
            self.img = pygame.transform.scale(self.img, (50,50))
            return self.img

    def update(self):
        self.rect.topleft = self.pos