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
#NECESSARIO PARA DESENHAR A PECA E MOVIMENTALA COM O MOUSE. SEMPRE DEVE CONTER APENAS 1 SPRITE.
selected_piece_group = pygame.sprite.Group()

black_pieces_group = pygame.sprite.Group()
white_pieces_group = pygame.sprite.Group()
black_pieces_group.add(Peca('preta', (25,25)))
black_pieces_group.add(Peca('preta', (160,25)))
black_pieces_group.add(Peca('preta', (290,25)))
black_pieces_group.add(Peca('preta', (430,25)))
black_pieces_group.add(Peca('preta', (90,92)))
black_pieces_group.add(Peca('preta', (225,92)))
black_pieces_group.add(Peca('preta', (365,92)))
black_pieces_group.add(Peca('preta', (495,92)))
black_pieces_group.add(Peca('preta', (25,160)))
black_pieces_group.add(Peca('preta', (160,160)))
black_pieces_group.add(Peca('preta', (290,160)))
black_pieces_group.add(Peca('preta', (430,160)))
white_pieces_group.add(Peca('branca', (87,490)))
white_pieces_group.add(Peca('branca', (225,490)))
white_pieces_group.add(Peca('branca', (360,490)))
white_pieces_group.add(Peca('branca', (490,490)))
white_pieces_group.add(Peca('branca', (25,435)))
white_pieces_group.add(Peca('branca', (160,435)))
white_pieces_group.add(Peca('branca', (290,435)))
white_pieces_group.add(Peca('branca', (425,435)))
white_pieces_group.add(Peca('branca', (87,365)))
white_pieces_group.add(Peca('branca', (225,365)))
white_pieces_group.add(Peca('branca', (360,365)))
white_pieces_group.add(Peca('branca', (490,365)))

#peca com que o jogador interage
selected_piece = None
old_position = None

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not menu.is_enabled():
            #Se uma peça estiver selecionada o clique do mouse vai soltar a peça na posição atual.
            if selected_piece != None:
                selected_piece_group.remove(selected_piece)
                if selected_piece.__getattribute__('cor') == 'branca':
                    white_pieces_group.add(selected_piece)
                    selected_piece = None
                else:
                    black_pieces_group.add(selected_piece)
                    selected_piece = None
            #Se não há uma peca selecionada procurar por uma peca que esteja em baixo do ponteiro do mouse.
            else:    
                for p in white_pieces_group.sprites():
                    if p.rect.collidepoint(event.pos) and selected_piece == None:
                        selected_piece = p
                        selected_piece_group.add(p)
                        white_pieces_group.remove(p)

                for p in black_pieces_group.sprites():
                    if p.rect.collidepoint(event.pos) and selected_piece == None:
                        selected_piece = p
                        selected_piece_group.add(p)
                        black_pieces_group.remove(p)

    if selected_piece != None:
        selected_piece.__setattr__('pos', tuple(pygame.mouse.get_pos()))

    if menu.is_enabled():
        try:
            menu.update(events)
            menu.draw(screen)
        except:
            pass
    else:
        screen.blit(board, (0,0))
        if selected_piece != None:
            selected_piece.update()
            selected_piece_group.draw(screen)
            
        white_pieces_group.draw(screen)
        black_pieces_group.draw(screen)
        black_pieces_group.update()
        white_pieces_group.update()

    pygame.display.update()
