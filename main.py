import pygame
import pygame_menu

pygame.init()

icon = pygame.image.load('img/checkers.png')
board = pygame.image.load('img/checkers_board.jpg')
screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)
menu = pygame_menu.Menu(300, 400, 'Damas',theme=pygame_menu.themes.THEME_DARK)
menu.add_button('Play', menu.disable)
menu.add_button('Quit', pygame_menu.events.EXIT)
#GameLoop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    #Exception ocorre ao dar Play no jogo pois o IF ainda esta rodando (CONSERTAR DEPOIS)
    if menu.is_enabled():
        try:                    
            menu.update(events)
            menu.draw(screen)
        except:
            pass
    else:
        screen.blit(board, (0,0))
    pygame.display.update()
