import pygame
import pygame_menu
from Peca import Peca

pygame.init()

icon = pygame.image.load('img/checkers.png')
board = pygame.image.load('img/checkers_board.jpg')
screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("Damas")
pygame.display.set_icon(icon)
menu = pygame_menu.Menu(520, 520, 'Damas', onclose=pygame_menu.events.EXIT, theme=pygame_menu.themes.THEME_DARK)
menu.add_button('Play', menu.disable)
menu.add_button('Quit', pygame_menu.events.EXIT)

#GameLoop
running = True

#Criar pecas
black_pieces_group = pygame.sprite.Group()
white_pieces_group = pygame.sprite.Group()
black_pieces_group.add(Peca('preta', (0,0)))
black_pieces_group.add(Peca('preta', (135,0)))
black_pieces_group.add(Peca('preta', (265,0)))
black_pieces_group.add(Peca('preta', (405,0)))
black_pieces_group.add(Peca('preta', (65,67)))
black_pieces_group.add(Peca('preta', (200,67)))
black_pieces_group.add(Peca('preta', (340,67)))
black_pieces_group.add(Peca('preta', (470,67)))
black_pieces_group.add(Peca('preta', (0,135)))
black_pieces_group.add(Peca('preta', (135,135)))
black_pieces_group.add(Peca('preta', (265,135)))
black_pieces_group.add(Peca('preta', (405,135)))
white_pieces_group.add(Peca('branca', (62,465)))
white_pieces_group.add(Peca('branca', (200,465)))
white_pieces_group.add(Peca('branca', (335,465)))
white_pieces_group.add(Peca('branca', (465,465)))
white_pieces_group.add(Peca('branca', (0,410)))
white_pieces_group.add(Peca('branca', (135,410)))
white_pieces_group.add(Peca('branca', (265,410)))
white_pieces_group.add(Peca('branca', (400,410)))
white_pieces_group.add(Peca('branca', (62,340)))
white_pieces_group.add(Peca('branca', (200,340)))
white_pieces_group.add(Peca('branca', (335,340)))
white_pieces_group.add(Peca('branca', (465,340)))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not menu.is_enabled():
            for p in black_pieces_group.sprites():
                if p.rect.collidepoint(event.pos):
                    position = p.__getattribute__('pos')
                    pos = list(position)
                    pos[0] += 15
                    pos[1] += 15
                    position = tuple(pos)
                    p.__setattr__('pos', position)
                else:
                    pass

            for p in white_pieces_group.sprites():
                if p.rect.collidepoint(event.pos):
                    position = p.__getattribute__('pos')
                    pos = list(position)
                    pos[0] += 15
                    pos[1] += 15
                    position = tuple(pos)
                    p.__setattr__('pos', position)
                else:
                    pass

    if menu.is_enabled():
        try:
            menu.update(events)
            menu.draw(screen)
        except:
            pass
    else:
        screen.blit(board, (0,0))
        white_pieces_group.draw(screen)
        black_pieces_group.draw(screen)
        black_pieces_group.update()
        white_pieces_group.update()

    pygame.display.update()
