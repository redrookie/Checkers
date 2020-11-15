import pygame
import pygame_menu
from Jogo import Jogo

pygame.init()

icon = pygame.image.load('img/checkers.png')
board = pygame.image.load('img/checkers_board.jpg')
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)


######################## TABULEIRO


game_theme = pygame_menu.themes.THEME_DARK.copy()
game = pygame_menu.Menu(700, 700, 
                        onclose=pygame_menu.events.DISABLE_CLOSE,
                        theme=game_theme,
                        title = 'Match')

game.add_image('img/checkers_board.jpg',
                     align = pygame_menu.locals.ALIGN_CENTER)                    

game.add_button('Give Up', pygame_menu.events.BACK, align = pygame_menu.locals.ALIGN_CENTER)



########################## MENU
menu = pygame_menu.Menu(700, 700, 'Damas',theme=pygame_menu.themes.THEME_DARK, onclose=pygame_menu.events.EXIT)
menu.add_button('Play', game, align=pygame_menu.locals.ALIGN_RIGHT)
menu.add_selector('Difficulty',  [('Easy', 'EASY'),
                                ('Medium', 'MEDIUM'),
                                ('Hard', 'HARD')], selector_id='difficulty', default=1, align=pygame_menu.locals.ALIGN_RIGHT)

menu.add_button('Quit', pygame_menu.events.EXIT, align=pygame_menu.locals.ALIGN_RIGHT)


#GameLoop
running = True
jogo = Jogo()




while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
                        

    menu.update(events)
    menu.draw(screen)
    jogo.desenha_tabuleiro(screen)
    pygame.display.update()
