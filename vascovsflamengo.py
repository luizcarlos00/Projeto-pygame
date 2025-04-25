import pygame
import imagens,audio
from pygame.locals import *
from sys import exit
from modulo import construir_grid
from posiciona import posicionar
from turno import turno


def main():
    pygame.init()
    

    musica_menu=pygame.mixer.music.load("audio/musica_fundo.wav")
    #musica_jogo=pygame.mixer.music.load("musica_fundo_jogo.wav")
    bomba_agua=pygame.mixer.Sound("audio/acerto_agua.wav")
    bomba_barco=pygame.mixer.Sound("audio/acerto_barco.wav")
    


    
    jogador1 = []
    jogador2 = []
    marcadosJ1=[]
    marcadosJ2=[]
    vencedor = "?"
    condicaoJ1=[]
    condicaoJ2=[]
    tela=pygame.display.set_mode((1200,1000))#definição de tela
    relogio = pygame.time.Clock()
    tela.blit(pygame.transform.scale(pygame.image.load("imagens/tela_fundo_menu.png"),(1200,1000)),(0,0))
    construir_grid(tela,1200)#função que desenha e e faz a tupla dos quadrados
    pygame.display.flip()


    barco1=pygame.image.load("imagens/barco1.png")
    barco2_v=pygame.image.load("imagens/barco2_v.png")
    barco2_h=pygame.image.load("imagens/barco2_h.png")
    barco3_v=pygame.image.load("imagens/barco3_v.png")
    barco3_h=pygame.image.load("imagens/barco3_h.png")
    barco4_h=pygame.image.load("imagens/barco4_h.png")
    barco4_v=pygame.image.load("imagens/barco4_h.png")





    
    while True:
        pygame.mixer.music.play(-1)
        relogio.tick(60)
        for event in pygame.event.get():#sair 
            if event.type== QUIT:
                pygame.quit()
                exit()

            if jogar==0:
                if event.type==MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pos()[0]//100)<=3 and (pygame.mouse.get_pos()[1]//100)==8:#iniciar o jogo 
                            jogar=1
                    if (pygame.mouse.get_pos()[0]//100)<=3 and (pygame.mouse.get_pos()[1]//10)<=96 and (pygame.mouse.get_pos()[1]//10)>=90:#menu instruções depois fazer o resto
                            instrucoes=1

            if jogar==1:
                if jogador1 == [] and jogador2 == []:
                    jogador1 = posicionar(jogador1)
                    tela.fill((0,0,255))
                    construir_grid(tela, 1200)
                    pygame.display.flip
        
                    jogador2 = posicionar(jogador2)
                    tela.fill((0,0,255))
                    construir_grid(tela, 1200)
                    pygame.display.flip

                
            
                
                            
            else:
                
                while vencedor == "?":
                    jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2 = turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2)
                    

                    
                  
                    if len(condicaoJ1) == 10:
                        vencedor = "jogador1"
                    
                    
                    if len(condicaoJ2) == 10:
                        vencedor = "jogador2"
                print(vencedor)    
                
                
            if jogar==2:
                tela.blit(pygame.image.load("tela_creditos.png")
                          if event.key==K_j:
                                jogar=0
                


        
       

        pygame.display.flip()


if __name__=="__main__":
    main()
    
