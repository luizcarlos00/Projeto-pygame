import pygame
import modulo as construir_grid

def posicionar( jogador=[]):
    while len(jogador) < 8:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                        print(pygame.mouse.get_pos())
                        posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                        jogador.append(posicao)
                        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100))
                        pygame.display.flip()