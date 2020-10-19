import pygame

pygame.init()


icon = pygame.image.load('checkers.png')
board = pygame.image.load('checkers_board.png')
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)



#GameLoop

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(board, (0,0))
    pygame.display.update()