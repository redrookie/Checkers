import pygame
import pygame_menu
from Jogo import Jogo

def disable_menu(screen, board):
    menu.disable()
    screen.blit(board, (0, 0))

pygame.init()

icon = pygame.image.load('img/checkers.png')
board = pygame.image.load('img/checkers_board.jpg')
screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)
menu = pygame_menu.Menu(520, 520, 'Damas',theme=pygame_menu.themes.THEME_DARK)
menu.add_button('Play', disable_menu, screen, board)
menu.add_button('Quit', pygame_menu.events.EXIT)
#GameLoop
running = True
jogo = Jogo()
mouse_pos = [(0,0),(0,0)] # Pos antiga e nova do click do mouse para movimentar as pecas
count_clicks = 0 # Quando 2 clicks forem contados, movimenta a peca de mouse_pos[0] para mouse_pos[1]

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not menu.is_enabled():
            pos = pygame.mouse.get_pos()
            count_clicks += 1
            if count_clicks == 1:
                mouse_pos[0] = pos
            elif count_clicks == 2:
                mouse_pos[1] = pos
                count_clicks = 0
                print(mouse_pos)
                jogo.movimenta_peca(screen, mouse_pos)
    #Exception ocorre ao dar Play no jogo pois o IF ainda esta rodando (CONSERTAR DEPOIS)
    if menu.is_enabled():
        try:
            menu.update(events)
            menu.draw(screen)
        except:
            pass
    else:
        jogo.desenha_tabuleiro(screen)
    pygame.display.update()
