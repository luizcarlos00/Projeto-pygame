import pygame
from modulo import construir_grid
# adicionar imagem para quadrados não selecionados e selecionados
def turno(jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2):
    j1OK = False
    j2OK= False
    vez = True

    barco1=pygame.image.load("imagens/barco1.png")
    barco2_v=pygame.image.load("imagens/barco2_v.png")
    barco2_h=pygame.image.load("imagens/barco2_h.png")
    barco3_v=pygame.image.load("imagens/barco3_v.png")
    barco3_h=pygame.image.load("imagens/barco3_h.png")
    barco4_h=pygame.image.load("imagens/barco4_h.png")
    barco4_v=pygame.image.load("imagens/barco4_v.png")
    
    while True:
        for event in pygame.event.get():#sair 
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
            if vez :
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                construir_grid(pygame.display.get_surface(),1200)
                if len(condicaoJ1) > 0:
                    for barco in condicaoJ1:
                        if len(barco) == 4:
                            if barco[0][0] - barco[1][0] == 0:
                                imagem = barco4_v
                            else:
                                imagem = barco4_h
                        elif len(barco) == 3:
                            if barco[0][0] - barco[1][0] == 0:
                                imagem = barco3_v
                            else:
                                imagem = barco3_h
                        elif len(barco) == 2:
                            if barco[0][0] - barco[1][0] == 0:
                                imagem = barco2_v
                            else:
                                imagem = barco2_h
                        else:
                            imagem = barco1
                        pygame.display.get_surface().blit(imagem,(barco[0][0]*100,barco[0][1]*100))
                pygame.display.flip()

                if posicao not in marcadosJ1 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                    for barco in jogador2:
                        if posicao in barco:
                            condicaoJ1.append(barco)
                            for coord in barco:
                                marcadosJ1.append(coord)
                            break
                        
                    if posicao not in marcadosJ1:
                        marcadosJ1.append(posicao)
                                                               
                    j1OK = True
                    vez = not vez
                   # pygame.display.get_surface().blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                    pygame.display.get_surface().fill((0,0,255))
                
            else:
                
                posicao=(pygame.mouse.get_pos()[0]//100,pygame.mouse.get_pos()[1]//100)
                construir_grid(pygame.display.get_surface(),1200)
                if len(condicaoJ1) > 0:
                    for barco in condicaoJ2:
                        if barco != None:    
                            if len(barco) == 4:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco4_v
                                else:
                                    imagem = barco4_h
                            elif len(barco) == 3:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco3_v
                                else:
                                    imagem = barco3_h
                            elif len(barco) == 2:
                                if barco[0][0] - barco[1][0] == 0:
                                    imagem = barco2_v
                                else:
                                    imagem = barco2_h
                            else:
                                imagem = barco1
                        pygame.display.get_surface().blit(imagem,(barco[0][0]*100,barco[0][1]*100))
                pygame.display.flip()
                if posicao not in marcadosJ2 and posicao[0] >= 2:
                    construir_grid(pygame.display.get_surface(),1200)
                    pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(posicao[0]*100,posicao[1]*100,100,100),(2))
                    pygame.display.flip()

                if event.type==pygame.MOUSEBUTTONDOWN:#pegar a posição do mouse na tela
                    
                    for barco in jogador1:
                        if posicao in barco:
                            condicaoJ2.append(barco)
                            for coord in barco:
                                marcadosJ2.append(coord)
                            break

                    if posicao not in marcadosJ2:
                        marcadosJ2.append(posicao)
                    
                    
                    j2OK = True
                    vez = not vez
                    #pygame.display.get_surface().blit(pygame.image.load("tela_fundo.jpg"),(0,0))
                    pygame.display.get_surface().fill((0,0,255))  
        if j1OK and j2OK:
            return jogador1,jogador2,marcadosJ1,marcadosJ2,condicaoJ1,condicaoJ2
            