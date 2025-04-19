import pygame
from pygame.locals import *
from sys import exit
from modulo import construir_grid
from posiciona import posicionar

def main():
    pygame.init()
    largura=1200
    altura=1000
    tela=pygame.display.set_mode((largura,altura))#definição de tela
    lista_pos=[(x,y) for x in range(10) for y in range(10)]
    relogio = pygame.time.Clock()
    jogador = []
    tela.blit(pygame.image.load("tela_fundo.jpg"),(0,0))
    barcos=0
    construir_grid(tela,largura)#função que desenha e e faz a tupla dos quadrados
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
    
            if len(jogador) < 11:
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                if barcos == 0 and posicao[0] <=8:
                    if posicao[0] in range(2,13):
                        construir_grid(tela,largura)
                        pygame.draw.rect(tela,(255,0,0),(posicao[0]*100,posicao[1]*100,400,100),(2)) # desenha um retangulo de mesmas dimensões no quadrado que o jogador está com o mouse                  
                    if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                        posicionou = [(x,posicao[1]) for x in range(posicao[0],posicao[0]+4)]
                        jogador.append(posicionou)
                        pygame.draw.rect(tela,(0,0,0),(posicao[0]*100,posicao[1]*100,400,100))
                        barcos +=1

                elif barcos in range(1,3) and posicao[0] <=9 and posicao not in jogador[len(jogador)-1]:
                        if posicao[0] in range(2,13):
                            construir_grid(tela,largura)
                            pygame.draw.rect(tela,(255,0,0),(posicao[0]*100,posicao[1]*100,300,100),(2))
                        if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                            posicionou = [(x,posicao[1]) for x in range(posicao[0],posicao[0]+3)]
                            jogador.append(posicionou)
                            pygame.draw.rect(tela,(0,0,0),(posicao[0]*100,posicao[1]*100,300,100))
                            barcos +=1
                
                elif barcos in range(3,6) and posicao[0] <=10 and posicao not in jogador[len(jogador)-1]:
                        if posicao[0] in range(2,13):
                            construir_grid(tela,largura)
                            pygame.draw.rect(tela,(255,0,0),(posicao[0]*100,posicao[1]*100,200,100),(2))
                        if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                            posicionou = [(x,posicao[1]) for x in range(posicao[0],posicao[0]+2)]
                            jogador.append(posicionou)
                            pygame.draw.rect(tela,(0,0,0),(posicao[0]*100,posicao[1]*100,200,100))
                            barcos +=1

                elif barcos in range(6,10) and posicao not in jogador[len(jogador)-1]:
                        if posicao[0] in range(2,13):
                            construir_grid(tela,largura)
                            pygame.draw.rect(tela,(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                        if event.type==MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                            jogador.append(posicao)
                            pygame.draw.rect(tela,(0,0,0),(posicao[0]*100,posicao[1]*100,100,100))
                            barcos +=1
                            
                        
                            
                print(jogador)


        
        
        
        
        
        
        
        
        pygame.display.flip()


if __name__=="__main__":
    main()
    