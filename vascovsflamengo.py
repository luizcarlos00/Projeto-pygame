import pygame
from pygame.locals import *
from sys import exit
from modulo import construir_grid
from posiciona import posicionar
from turno import turno

def main():
    pygame.init()
    tela=pygame.display.set_mode((1200,1000))#definição de tela
    relogio = pygame.time.Clock()
    jogador1 = []
    jogador2 = []
    marcadosJ1=[]
    marcadosJ2=[]
    vencedor = "?"
    tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
    construir_grid(tela,1200)#função que desenha e e faz a tupla dos quadrados
    pygame.display.flip()
    while True:
        relogio.tick(60)
        for event in pygame.event.get():#sair 
            if event.type== QUIT:
                pygame.quit()
                exit()
                
            if jogador1 == [] and jogador2 == []:
                jogador1 = posicionar(jogador1)
                tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                construir_grid(tela, 1200)
                pygame.display.flip

                jogador2 = posicionar(jogador2)
                tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                construir_grid(tela, 1200)
                pygame.display.flip
                
                condicaoJ1 = []
                for barco in jogador2:
                    for coord in barco:
                        condicaoJ1.append(coord)
                
                condicaoJ2 = []
                for barco in jogador1:
                    for coord in barco:
                        condicaoJ2.append(coord)
            
            else:
                
                while vencedor == "?":
                    jogador1,jogador2,marcadosJ1,marcadosJ2 = turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2)
                    
                    
                    acertosJ1 = 0
                    for coord in condicaoJ1:
                        if coord in marcadosJ1:
                            acertosJ1+= 1
                    
                    if acertosJ1 == len(condicaoJ1):
                        vencedor = "jogador1"
                    print(acertosJ1, len(condicaoJ1))
                    acertosJ2 = 0
                    for coord in condicaoJ2:
                        if coord in marcadosJ2:
                            acertosJ2 += 1

                    if acertosJ2 == len(condicaoJ2):
                        vencedor = "jogador2"
                    print(acertosJ2, len(condicaoJ2))
                print(vencedor)
            
        pygame.display.flip()


if __name__=="__main__":
    main()
    