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
piece_to_kill_group = pygame.sprite.Group()
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

#peca com que o jogador interage.
selected_piece = None
piece_to_kill = None

#posicao antiga da peca selecionada.
old_position = None

#True para o turno das pecas brancas, False para o turno das pecas pretas.
turno = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                menu.enable()
                black_pieces_group.empty()
                white_pieces_group.empty()
                selected_piece = None
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not menu.is_enabled():
            #Se uma peça estiver selecionada, nao estiver na mesma posição de outra peca, e tiver se movido na diagonal, o clique do mouse vai soltar a peça na posição atual.
            if selected_piece != None:
                if (not pygame.sprite.spritecollide(selected_piece, white_pieces_group, False) and 
                    not pygame.sprite.spritecollide(selected_piece, black_pieces_group, False) and
                    abs(selected_piece.__getattribute__('pos')[0] - old_position[0]) > 40 and 
                    (selected_piece.__getattribute__('pos')[1] - old_position[1] < 0 or selected_piece.__getattribute__('promoted') or selected_piece.__getattribute__('cor') == 'preta') and 
                    (selected_piece.__getattribute__('pos')[1] - old_position[1] > 0 or selected_piece.__getattribute__('promoted') or selected_piece.__getattribute__('cor') == 'branca') and 
                    (abs(selected_piece.__getattribute__('pos')[0] - old_position[0]) < 80 or piece_to_kill != None or selected_piece.__getattribute__('promoted')) and
                    (abs(selected_piece.__getattribute__('pos')[0] - old_position[0]) < 145 or selected_piece.__getattribute__('promoted')) and
                    (abs(selected_piece.__getattribute__('pos')[1] - old_position[1]) < 145 or selected_piece.__getattribute__('promoted')) and
                    (abs(selected_piece.__getattribute__('pos')[1] - old_position[1]) < 80 or piece_to_kill != None or selected_piece.__getattribute__('promoted'))):
                    
                    #Muda o turno.
                    turno = not turno
                    
                    #solta a peca se for branca
                    if selected_piece.__getattribute__('cor') == 'branca':
                        if(selected_piece.__getattribute__('pos')[1] < 53):
                            selected_piece.promote()
                        white_pieces_group.add(selected_piece)
                    #solta a peca se for preta
                    else:
                        if(selected_piece.__getattribute__('pos')[1] > 470):
                            selected_piece.promote()
                        black_pieces_group.add(selected_piece)
                        

                    if piece_to_kill != None:
                        piece_to_kill_group.empty()
                        piece_to_kill.kill()
                    
                    selected_piece_group.remove(selected_piece)
                    selected_piece = None

                else:#Movimento invalido, solta a peca na posicao original
                    selected_piece.__setattr__('pos', old_position)
                    piece_to_kill_group.empty()
                    piece_to_kill = None

                    #solta a peca se for branca
                    if selected_piece.__getattribute__('cor') == 'branca':
                        white_pieces_group.add(selected_piece)
                        selected_piece = None
                    
                    #solta a peca se for preta
                    else:
                        black_pieces_group.add(selected_piece)
                        selected_piece = None
            #Se não há uma peca selecionada procurar por uma peca que esteja em baixo do ponteiro do mouse.
            else:    
                #turno das pecas pretas
                if not turno:
                    for p in black_pieces_group.sprites():
                        if p.rect.collidepoint(event.pos) and selected_piece == None:
                            selected_piece = p
                            old_position = p.__getattribute__('pos')
                            selected_piece_group.add(p)
                            black_pieces_group.remove(p)
                #turno das pecas brancas
                else:
                    for p in white_pieces_group.sprites():
                        if p.rect.collidepoint(event.pos) and selected_piece == None:
                            selected_piece = p
                            old_position = p.__getattribute__('pos')
                            selected_piece_group.add(p)
                            white_pieces_group.remove(p)

    if selected_piece != None:
        #Atualiza a posição da peca selecionada a cada frame.
        selected_piece.__setattr__('pos', tuple(pygame.mouse.get_pos()))
        #Escolhe uma peca para destruir
        # print(selected_piece.__getattribute__('pos'))
        if (selected_piece.__getattribute__('cor') == 'branca' and pygame.sprite.spritecollide(selected_piece, black_pieces_group, False)):
            for p in black_pieces_group.sprites():
                piece_to_kill_group.add(p)
                if pygame.sprite.spritecollide(selected_piece, piece_to_kill_group, False):
                    piece_to_kill = p
                piece_to_kill_group.remove(p)
        if (selected_piece.__getattribute__('cor') == 'preta' and pygame.sprite.spritecollide(selected_piece, white_pieces_group, False)):
            for p in white_pieces_group.sprites():
                piece_to_kill_group.add(p)
                if pygame.sprite.spritecollide(selected_piece, piece_to_kill_group, False):
                    piece_to_kill = p
                piece_to_kill_group.remove(p)

    
    #Metodos para desenhar os objetos na janela
    if menu.is_enabled():
        try:
            menu.update(events)
            menu.draw(screen)
        except:
            pass
    else:
        #A ordem de draw e importante
        screen.blit(board, (0,0))
        if selected_piece != None:
            selected_piece.update()
            selected_piece_group.draw(screen)
            
        white_pieces_group.draw(screen)
        black_pieces_group.draw(screen)
        black_pieces_group.update()
        white_pieces_group.update()
        if(not menu.is_enabled() and selected_piece == None and (len(black_pieces_group.sprites()) == 0 or len(white_pieces_group.sprites()) == 0)):
            print("game ended")
            menu.enable()
            black_pieces_group.empty()
            white_pieces_group.empty()
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

    pygame.display.update()
