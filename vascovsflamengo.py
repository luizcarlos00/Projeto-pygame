import pygame
from pygame.locals import *
from sys import exit
from modulo import construir_grid
from posiciona import posicionar

def main():
    pygame.init()
    tela=pygame.display.set_mode((1200,1000))#definição de tela
    relogio = pygame.time.Clock()
    jogador1 = []
    jogador2 = []
    tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
    construir_grid(tela,1200)#função que desenha e e faz a tupla dos quadrados
    pygame.display.flip()
    while True:
        relogio.tick(60)
        for event in pygame.event.get():#sair 
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                print(pygame.mouse.get_pos())
                ret=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                print(ret)
                print(pygame.display.get_surface())
            if jogador1 == [] and jogador2 == []:
                jogador1 = posicionar(jogador1)
                tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                construir_grid(tela, 1200)
                pygame.display.flip

                jogador2 = posicionar(jogador2)
                tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                construir_grid(tela, 1200)
                pygame.display.flip
                print (jogador1, jogador2)
                

            
        pygame.display.flip()


if __name__=="__main__":
    main()
    