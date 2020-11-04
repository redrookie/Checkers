import pygame
import pygame_menu

pygame.init()

icon = pygame.image.load('img/checkers.png')
board = pygame.image.load('img/checkers_board.jpg')
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)

game_theme = pygame_menu.themes.THEME_DARK.copy()
game_theme.widget_alignment = pygame_menu.locals.ALIGN_RIGHT

game = pygame_menu.Menu(600, 800, 
                        onclose=pygame_menu.events.DISABLE_CLOSE,
                        theme=game_theme,
                        title = 'Match')

game.add_image('img/checkers_board.jpg',
                     align = pygame_menu.locals.ALIGN_LEFT)                    

game.add_button('Give Up', pygame_menu.events.BACK)

menu = pygame_menu.Menu(600, 800, 'Damas',theme=pygame_menu.themes.THEME_DARK, onclose=pygame_menu.events.EXIT)
menu.add_button('Play', game, align=pygame_menu.locals.ALIGN_RIGHT)
menu.add_selector('Difficulty',  [('Easy', 'EASY'),
                                ('Medium', 'MEDIUM'),
                                ('Hard', 'HARD')], selector_id='difficulty', default=1, align=pygame_menu.locals.ALIGN_RIGHT)

menu.add_button('Quit', pygame_menu.events.EXIT, align=pygame_menu.locals.ALIGN_RIGHT)
#GameLoop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
                        
    #Exception ocorre ao dar Play no jogo pois o IF ainda esta rodando (CONSERTAR DEPOIS)
    #if menu.is_enabled():
    #    try:                    
    #        menu.update(events)
    #        menu.draw(screen)
    #    except:
    #        pass
    #else:
    #    screen.blit(board, (0,0))
    menu.update(events)
    menu.draw(screen)
    pygame.display.update()
