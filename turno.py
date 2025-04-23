import pygame
from modulo import construir_grid

def turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2):
    j1OK = False
    j2OK= False
    vez = True
    while True:
        for event in pygame.event.get():#sair 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
            if vez :
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                construir_grid(pygame.display.get_surface(),1200)
                pygame.display.flip()
                for marcado in marcadosJ1:
                    pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(marcado[0]*100,marcado[1]*100,100,100))
                    pygame.display.flip()
                if posicao not in marcadosJ1 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                    for barco in jogador2:
                        if posicao in barco:
                            for coord in barco:
                                marcadosJ1.append(coord)
                            break
                        
                    if posicao not in marcadosJ1:
                        marcadosJ1.append(posicao)
                                                               
                    j1OK = True
                    vez = not vez
                    pygame.display.get_surface().blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                
            else:
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                construir_grid(pygame.display.get_surface(),1200)
                pygame.display.flip()
                for marcado in marcadosJ2:
                    pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(marcado[0]*100,marcado[1]*100,100,100))
                    pygame.display.flip()
                if posicao not in marcadosJ2 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                    
                    for barco in jogador1:
                        if posicao in barco:
                            for coord in barco:
                                marcadosJ2.append(coord)
                            break

                    if posicao not in marcadosJ2:
                        marcadosJ2.append(posicao)
                    
                    
                    j2OK = True
                    vez = not vez
                    pygame.display.get_surface().blit(pygame.image.load("tela_fundo.jpg"),(0,0))  
        if j1OK and j2OK:
            return jogador1,jogador2,marcadosJ1,marcadosJ2
            